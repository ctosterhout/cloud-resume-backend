const puppeteer = require('puppeteer');
const { DOMAIN_NAME } = require('../config.json');

const sleep = async (r) => await new Promise(r => setTimeout(r, 100));

(async () => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    const website = `http://myresume.${DOMAIN_NAME}`
    console.log(`Loading: ${website}`)
    await page.goto(website)
    console.log(`Waiting for API calls to be made`)
    await sleep(100)
    const element = await page.$("#visitors")
    const property = await element.getProperty('innerHTML');
    const count = await property.jsonValue();
    console.log(`Getting page element, count: ${count}`)
    if (!count) {
        throw new Error("Cannot find count value")
    } else {
        console.log("PASS");
    }
    await browser.close();
})();