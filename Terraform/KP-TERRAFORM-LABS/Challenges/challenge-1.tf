provider "aws" {
 region = "eu-west-2"
}


resource "aws_eip" "kplabs_app_ip" {
    domain   = "vpc"
}
