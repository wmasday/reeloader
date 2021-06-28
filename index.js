const clc = require("cli-color");
const prompt = require('prompt-sync')();
const axios = require('axios');
const got = require("got");
const { createWriteStream } = require("fs");

console.log("");
console.log(clc.cyan("\t\t===[ Instagram Reels Downloader ]==="));
console.log(clc.cyan("\t\t\tgithub.com/akuhidayat"));
console.log("");

const url = prompt(clc.white("[?] Url\t : "));
axios.get(url)
.then(function(response){
    const regex = response.data.match('"video_url":"(.*)","video_view_count"')[1];
    const result_url = decodeURIComponent(JSON.parse('"' + regex.replace(/\"/g, '\\"') + '"'));
    const name = prompt("[?] Filename\t : ");
    got.stream(result_url).pipe(createWriteStream(name));
    console.log(clc.green("[!] Download Success!"));
    console.log(clc.white(""));
})
.catch(function (error) {
    console.log(error);
});

