
provider "oci" {
  tenancy_ocid = var.tenancy_ocid
  user_ocid    = var.user_ocid
  fingerprint  = var.fingerprint
  private_key_path = var.private_key_path
  region       = var.region
}

resource "oci_functions_function" "rag_api" {
  application_id = oci_functions_application.rag_app.id
  display_name   = "RAGAPI"
  image          = "ocir.io/yourrepo/rag-system:latest"
}

resource "oci_apigateway_api" "rag_api_gw" {
  compartment_id = var.compartment_id
  display_name   = "RAG API Gateway"
  route_prefix   = "/api"
}
