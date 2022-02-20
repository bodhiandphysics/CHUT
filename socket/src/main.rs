use serde::{Deserialize, Serialize};
use std::fs::File;
use std::io::{BufReader, BufWriter, Write};
use tokio::{
    net::{TcpListener, TcpStream},
    task,
};

// const ADDR: &'static str = "127.0.0.1:8080";
const ADDR: &'static str = "20.127.111.209:8080";
const DIR: &'static str = "../../data/sched";

#[derive(Serialize, Deserialize, Debug)]
struct Times {
    year: usize,
    month: String,
    day: String,
    hour: String,
    minute: String,
    direction: String,
    line: String,
    station: String,
}

#[derive(Serialize, Deserialize, Debug)]
#[serde(transparent)]
struct Station {
    times: Vec<Times>,
}

#[tokio::main]
async fn main() -> Result<(), futures::io::Error> {
    let listener = TcpListener::bind(&ADDR).await?;
    loop {
        let (stream, addy) = listener.accept().await?;
        if let Err(e) = task::spawn(async move { handle(stream).await.unwrap() }).await {
            println!("Connection failed with client at {addy}.\nReason: {e}");
        }
    }
}

async fn handle(stream: TcpStream) -> Result<(), futures::io::Error> {
    let mut buf = [0; 1024];
    stream.readable().await?;
    let times = process(&stream, &mut buf).await?.times;
    stream.writable().await?;
    send(times, stream).await
}

async fn send(times: Vec<Times>, stream: TcpStream) -> Result<(), futures::io::Error> {
    let mut writer = BufWriter::new(Vec::new());
    writer.write(&buff_from_usize(times.len())[..])?;
    stream.try_write(writer.buffer())?;
    writer.flush()?;
    for time in times {
        let json = serde_json::to_vec(&time)?;
        writer.write(&buff_from_usize(json.len())[..])?;
        writer.write(&json[..])?;
        stream.try_write(writer.buffer())?;
        writer.flush()?;
    }
    Ok(())
}

async fn process(stream: &TcpStream, buf: &mut [u8; 1024]) -> Result<Station, std::io::Error> {
    let n = stream.try_read(buf)?;
    let name = unsafe { std::str::from_utf8_unchecked(&buf[..n]) };
    Ok(serde_json::from_reader(BufReader::new(File::open(
        format!("{DIR}/{name}.json"),
    )?))?)
}

fn buff_from_usize(bytes: usize) -> [u8; 16] {
    let mut ret_buf = [48; 16];
    let mut n = bytes;
    let mut idx = 15;
    loop {
        let r = n % 10;
        n /= 10;
        if n == 0 && r == 0 {
            break;
        }
        ret_buf[idx] = (r + 48) as u8;
        idx -= 1;
    }
    ret_buf
}

#[cfg(test)]
mod tests {
    use super::buff_from_usize;
    #[test]
    fn numbers_to_cstring_test() {
        let ret_buff = buff_from_usize(32);
        let mut test_buf = [48; 16];
        test_buf[14] = 51;
        test_buf[15] = 50;
        assert_eq!(ret_buff, test_buf)
    }
    #[test]
    fn numbers_to_cstring_test2() {
        let ret_buff = buff_from_usize(17502);
        let mut test_buf = [48; 16];
        test_buf[15] = 2 + 48;
        test_buf[14] = 0 + 48;
        test_buf[13] = 5 + 48;
        test_buf[12] = 7 + 48;
        test_buf[11] = 1 + 48;
        assert_eq!(ret_buff, test_buf)
    }
}
