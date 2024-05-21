#[macro_use]
extern crate rocket;
use rocket::serde::json::{json, Value};
use uuid::Uuid;

#[get("/?<domain>")]
fn federation_provider(domain: Option<&str>) -> Value {
    let tenant_id = Uuid::new_v4();
    json!({
        "tenantId": tenant_id.to_string(),
        "authority_host": "127.0.0.1:8443",
        "graph": "https://127.0.0.1:8443",
    })
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .mount("/odc/v2.1/federationProvider", routes![federation_provider])
}
