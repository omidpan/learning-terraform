terraform {
  required_version = ">= 1.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 2.0"
    }
  }
}

provider "aws" {
  region = "us-west-2"
    assume_role {
    role_arn =  "arn:aws:iam::525024613134:role/assumer-redshift"
  }
}