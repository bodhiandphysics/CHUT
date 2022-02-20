use std::ffi::CString;
use std::fs::File;
use std::io::{BufReader, Read};
use tokio::net::{TcpListener, TcpStream};

const ADDR: &'static str = "127.0.0.1:8080";
const DIR: &'static str = "../../data/sched";

#[tokio::main]
async fn main() -> Result<(), futures::io::Error> {
    let mut buf = [0; 1024];
    let listener = TcpListener::bind(&ADDR).await?;
    loop {
        let (stream, _) = listener.accept().await.unwrap();
        stream.readable().await?;
        let result = process(&stream, &mut buf).await;
        dbg!(&result);
        let (bytes, string);
        if let Ok((b, s)) = result {
            bytes = b;
            string = s;
        } else {
            println!("Something went wrong here!");
            continue;
        }
        stream.writable().await?;
        stream
            .try_write(
                &buff_from_usize(bytes)
                    .iter()
                    .chain(string.as_bytes_with_nul())
                    .map(|b| *b)
                    .collect::<Vec<_>>()[..],
            )
            .unwrap();
        buf = [0; 1024];
    }
}

async fn process(
    stream: &TcpStream,
    buf: &mut [u8; 1024],
) -> Result<(usize, CString), std::io::Error> {
    loop {
        println!("HI");
        match stream.try_read(buf) {
            Ok(n) => {
                println!("HELLO");
                let name = unsafe { std::str::from_utf8_unchecked(&buf[..n]) };
                dbg!(&name);
                dbg!(format!("{}/{}.json", DIR, name));
                let file = File::open(format!("{}/{}.json", DIR, name))?;
                println!("HELLO");
                let mut reader = BufReader::new(file);
                let mut string_buff = Vec::new();
                match reader.read_to_end(&mut string_buff) {
                    Ok(bytes) => match CString::new(string_buff) {
                        Ok(cstring) => return Ok((bytes, cstring)),
                        Err(e) => {
                            dbg!(buf);
                            println!("GAH");
                            return Err(e.into());
                        }
                    },
                    Err(e) => {
                        dbg!(string_buff);
                        return Err(e.into());
                    }
                }
            }
            Err(ref e) if e.kind() == std::io::ErrorKind::WouldBlock => continue,
            Err(e) => {
                dbg!(&buf[..32]);
                println!("GAH");
                return Err(e.into());
            }
        }
    }
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
