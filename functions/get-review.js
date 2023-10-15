function main(params) {
  return new Promise(function (resolve, reject) {
    const { CloudantV1 } = require("@ibm-cloud/cloudant");
    const { IamAuthenticator } = require("ibm-cloud-sdk-core");
    const authenticator = new IamAuthenticator({
      apikey: "SlTWy6Td-PCy4vHd1fcUA69nZ7Coz5GAPuhHIj2Csnjr",
    });
    const cloudant = CloudantV1.newInstance({
      authenticator: authenticator,
    });
    cloudant.setServiceUrl("https://38085790-5dd4-4a5f-8128-e243a89ff7cf-bluemix.cloudantnosqldb.appdomain.cloud"); // TODO: Replace with your own service URL
    dealership = parseInt(params.dealerId);
    // return reviews with this dealer id
    cloudant
      .postFind({
        db: "reviews",
        selector: {
          dealership: parseInt(params.dealerId),
        },
      })
      .then((result) => {
        let code = 200;
        if (result.result.docs.length == 0) {
          code = 404;
        }
        resolve({
          statusCode: code,
          headers: { "Content-Type": "application/json" },
          body: result.result.docs,
        });
      })
      .catch((err) => {
        reject(err);
      });
  });
}

// example invocation
let result = main({ dealerId: 15 });
result.then((reviews) => console.log(reviews));
