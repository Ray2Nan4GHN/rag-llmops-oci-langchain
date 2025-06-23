##定义所需的 OCI Terraform 部署变量模板
variable "tenancy_ocid" {
  description = "OCI Tenancy OCID"
  type        = string
}

variable "user_ocid" {
  description = "OCI User OCID"
  type        = string
}

variable "fingerprint" {
  description = "API key fingerprint"
  type        = string
}

variable "private_key_path" {
  description = "Path to the private API key"
  type        = string
}

variable "region" {
  description = "OCI region"
  type        = string
}

variable "compartment_id" {
  description = "Compartment OCID for Functions and API Gateway"
  type        = string
}
