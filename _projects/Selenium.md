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

The entire end to end flow is automated, running on a regularly scheduled basis, allowing end users to simply review test results.


### Supported with

[![Eclipse][Eclipse.js]][Eclipse-url] [![Java][Java.js]][Java-url] [![Selenium][Selenium.js]][Selenium-url] [![GitHub][GitHub.js]][GitHub-url] [![Jenkins][Jenkins.js]][Jenkins-url]


<!-- TABLE OF CONTENTS -->
## Table of Contents
<ol>
  <li>
    <a href="#features">Features</a>
    <ul>
      <li><a href="#-cross-browser-compatability">Cross-Browser Compatability</a></li>
      <li><a href="#-extent-reports">Extent Reports</a></li>      
      <li><a href="#-json-test-paramatization">JSON Test Paramatization</a></li>
      <li><a href="#-takes-screenshot">Takes Screenshot</a></li>      
      <li><a href="#-page-object-model">Page Object Model</a></li>      
      <li><a href="#-javadoc-api">Javadoc API</a></li>      
      <li><a href="#-retries">Retries</a></li>      
      <li><a href="#-parallel-test">Parallel Test</a></li>      
      <li><a href="#-automated-test-execution">Automated Test Execution</a></li>   
      <li><a href="#-custom-test-execution">Custom Test Execution</a></li>    
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
<a id="extent-reports"></a>
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

[Check out the API](./doc/index.html)!

---
#### 🔁 Retries
Using TestNG IRetryAnalyzer we run any designated flaky test up to 3 times on failure, greatly improving our test accuracy.

---
#### 👩‍👩‍👦‍👦 Parallel Test
Setup to run tests on each website in parallel with simple controls to adjust capacity through test configuration XMLs.

---
#### ⏱️ Automated Test Execution
Test are run on a daily basis at midnight Eastern time through a local Jenkins server.

[See the latest report](./latestReport.html)!

<sub> Would have loved to have made this an online server, but web services can get expensive and locally hosting to the web is a network security risk I'm not suited to handle. </sub>

---
#### 🚀 Custom Test Execution
Using maven's surefire plugin, we can execute on test profiles to run fully customization tests. Current profiles can run each website separately or the full suite of test across all websites.

```
  pom.xml (abbrev.)
  <profile>
    <id>HumanBenchmark</id>
      <build>
      ...
        <suiteXmlFile>Test Suites/hbench.xml</suiteXmlFile>
      ...
    </build>
  </profile>


  hbench.xml
  <test thread-count="5" name="Human Benchmark Test">
    <classes>
      <class name="andrewSkye.tests.HumanBenchmarkTests" />
    </classes>
  </test>
```

<!-- SAMPLES -->
## Samples



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
