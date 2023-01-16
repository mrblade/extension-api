// Loading the dependencies. We don't need pretty
// because we shall not log html to the terminal
const axios = require("axios");
const cheerio = require("cheerio");
const fs = require("fs");

// URL of the page we want to scrape
const url = "https://www.inshorts.com/en/read";

// Async function which scrapes the data
async function scrapeData() {
  try {
    // Fetch HTML of the page we want to scrape
    const { data } = await axios.get(url);
    // Load HTML we fetched in the previous line
    const $ = cheerio.load(data);
    // Select all the list items in plainlist class
    const listItems = $(".news-card");
    // Stores data for all stories
    const stories = [];
    // Use .each method to loop through the li we selected
    listItems.each((idx, el) => {
      // Object holding data for each story/jurisdiction
      const story = { url: "", title: "", time: "" };

      
      // Select the text content of a and span elements
      // Store the textcontent in the above object
      story.title = $(el).find('.news-card-title .clickable span').text();
      story.time = $(el).find(".news-card-author-time-in-title .time").text();
      //story.url = $(el).find(".read-more a").attr('href') || null;
      story.url = $(el).find(".read-more a").attr('href') || "https://www.inshorts.com" + $(el).find(".news-card-title .clickable").attr('href');
      // Populate stories array with story data
      stories.push(story);
    });
    // Logs stories array to the console
    console.dir(stories);
    // Write stories array in stories.json file
    fs.writeFile("inshorts.json", JSON.stringify(stories, null, 2), (err) => {
      if (err) {
        console.error(err);
        return;
      }
      console.log("Successfully written data to file");
    });
  } catch (err) {
    console.error(err);
  }
}
// Invoke the above function
scrapeData();
