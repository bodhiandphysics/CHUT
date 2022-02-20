use std::ffi::CString;
use tokio::net::{TcpListener, TcpStream};

const ADDR: &'static str = "127.0.0.1:8080";

#[tokio::main]
async fn main() -> Result<(), futures::io::Error> {
    let listener = TcpListener::bind(&ADDR).await?;
    loop {
        let (stream, addy) = listener.accept().await?;
        let (bytes, string) = process(stream).await?;
    }
}

async fn process(stream: TcpStream) -> Result<(usize, CString), std::io::Error> {
    //! hello
}
