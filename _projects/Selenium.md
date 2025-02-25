---
layout: page
title: Selenium
description: an end to end automated web test
img: assets/img/12.jpg
importance: 1
category: personal
related_publications: false
---
<a id="readme-top"></a>

<!-- ABOUT THE PROJECT -->
## About The Project

This project is my personal Selenium playground. It goes through various practice automation sites, runs tests and generates comprehensive test reports.

The entire end to end flow is automated, running on a regularly scheduled basis, allowing users to simply review test results.


### Supported with

[![Eclipse][Eclipse.js]][Eclipse-url] [![Java][Java.js]][Java-url] [![Selenium][Selenium.js]][Selenium-url] [![GitHub][GitHub.js]][GitHub-url] [![Jenkins][Jenkins.js]][Jenkins-url] [![Python][Python.js]][Python-url]


<!-- TABLE OF CONTENTS -->
## Table of Contents
<ol>
  <li>
    <a href="#features">Features</a>
    <ul>
      <li><a href="#cross-browser-compatability">Cross-Browser Compatability</a></li>
      <li><a href="#extent-test">Extent Reports</a></li>      
      <li><a href="#extent-test">JSON Test Paramatization</a></li>
      <li><a href="#extent-test">Takes Screenshot</a></li>      
      <li><a href="#extent-test">Page Object Model</a></li>      
      <li><a href="#extent-test">Javadoc API</a></li>      
      <li><a href="#extent-test">Retries</a></li>      
      <li><a href="#extent-test">Parallel Test</a></li>      
      <li><a href="#extent-test">Automated Test Execution</a></li>   
      <li><a href="#extent-test">Custom Test Execution</a></li>    
    </ul>
  </li>
  <li><a href="#samples">Samples</a></li>
  <li><a href="#examples">Contact</a></li>
  <li><a href="#acknowledgments">Acknowledgments</a></li>
</ol>

<!-- FEATURES -->
## Features

#### 💻 Cross-Browser Compatability
Using Selenium WebDriver allows the tests to be run on any supported browser. Currently setup for Chrome, Firefox and Microsoft Edge.

```
    switch (browser) {
      case "chrome":
        driver = new ChromeDriver();
        break;
      case "firefox":
        driver = new FirefoxDriver();
        break;
      case "edge":
        driver = new EdgeDriver();
        break;
    }
```

---
#### 📊 Extent Reports
Generates comprehensive Extent Reports on every run with detailed logging.
![Example Report](./images/ExtentReportExample.png)

---
#### 📃 JSON Test Paramatization
Reads through JSON files to quickly customize and execute tests.
```
AddProductsToCart.json
[
  {
    "product":"Apple Cinema 30\"",
    "radio":"small",
    "checkbox":"checkbox 3",
    "text":"hello world",
    "select":"green",
    "date":"2021-05-11",
    "qty":"2"
  },
  {
    "product":"iPhone"
  },
  {
    "product":"iPod Shuffle",
    "qty":"3"
  }
]
```
![JSON Example](./images/JSONExample.png)
---
#### 📸 Takes Screenshot
Using TestNG Listeners, any time a test fails we take a screenshot of the failure state and attach it to the test report.

---
#### 📜 Page Object Model
Uses Page Factory with POM design pattern for clean, re-usable and easy to understand tests.
```
  @Test
  public void testTypingGame(ITestContext context) {
    HBMainPage mainPage = goToMainPage();
    TypingPage typingPage = mainPage.goToTypingPage();
    String paragraph = typingPage.getFullParagraph();
    int result = typingPage.typeTest(paragraph);
    Assert.assertTrue(result > 0, "Typing time displayed as below 0, " + result + "wpm");
  }
```
<sub> *Extent Test logging removed from above code snippit </sub>

---
#### 📚 Javadoc API
Fully documented with Javadocs.
[a link](./doc/index.html)

---
#### 🔁 Retries
Supports re-running failing tests multiple times when they are flaky

---
#### 👩‍👩‍👦‍👦 Parallel Test
Runs multiple tests in parallel to speed up execution time

---
#### ⏱️ Automated Test Execution
Ran on a regular basis through Jenkins, generating new reports daily.

---
#### 🚀 Custom Test Execution
Can execute on test profiles to run fully customizable tests. Current profiles written can run each website separately or every single test across all websites.
https://maven.apache.org/surefire/maven-surefire-plugin/

<!-- SAMPLES -->
## Samples

TBD

<!-- CONTACT -->
## Contact

Andrew Skye - andrew.d.skye@gmail.com

Project Link: [https://github.com/ASkye90/SeleniumPractice](https://github.com/ASkye90/SeleniumPractice)

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Udemy](https://www.udemy.com/) Selenium Java course used to start learning Selenium
* [Best-README-Template](https://github.com/othneildrew/Best-README-Template) used as starting framework for this README
* [Basic Selenium Project README](https://github.com/christian-draeger/basic-selenium-project/tree/master) inspired formatting for this README

  <p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png

[Java.js]: https://img.shields.io/badge/Java-%23ED8B00.svg?logo=openjdk&logoColor=white
[Java-url]: https://www.java.com/en/

[Selenium.js]: https://img.shields.io/badge/Selenium-43B02A?logo=selenium&logoColor=fff
[Selenium-url]: https://www.selenium.dev/

[GitHub.js]: https://img.shields.io/badge/GitHub-%23121011.svg?logo=github&logoColor=white
[GitHub-url]: https://github.com/

[Eclipse.js]: https://img.shields.io/badge/Eclipse-FE7A16.svg?logo=Eclipse&logoColor=white
[Eclipse-url]:  https://eclipseide.org/

[Jenkins.js]: https://img.shields.io/badge/Jenkins-D24939?logo=jenkins&logoColor=white
[Jenkins-url]: https://www.jenkins.io/

[Python.js]: https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff
[Python-url]: https://www.python.org/
