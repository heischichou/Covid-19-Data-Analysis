> [!NOTE] > **This project covers only the first seven months of 2020 since the original data set only contains data from January 2020 until July 2020.**

# Covid-19-Data-Analysis

My first Python Pandas ETL Pipeline.

## **Final Columns**

<details>
  <summary>These are the final columns comprising the ETL pipeline's resulting data set.</summary>

- **Country** - Country of the recorded case(s)
- **Lat** - Latitude of the location
  - _This column is retained only for Power BI Map visualizations._
- **Long** - Longitude of the location
  - _This column is retained only for Power BI Map visualizations._
- **Confirmed** - Cumulative number of confirmed cases until the given date
- **Deaths** - Cumulative number of deaths until the given date
- **Recovered** - Cumulative number of recovered cases until the given date
- **Active** - Cumulative number of active cases until the given date
- **WHO Region** - The WHO Region Code of the recorded case(s)
</details>

## **Grain Columns**

<details>
  <summary>These columns are implemented to introduce more granularity into the final data set.</summary>

- **Year** - Year of the cumulative report
- **Month** - Month of the cumulative report
- **Month Name** - Month name of the cumulative report
- **Day of Week** - Day of week of the cumulative report
- **Day Name** - Day name of the cumulative report
- **Month Short Name** - Short name of the month the cumulative report
</details>

## Research Questions

<details>
  <summary><strong>Cumulative Trends</strong></summary>
  <div>
    <p><i>What is the monthly trends of cumulative case outcomes?</i></p>
    <div align="center">
      <img src="https://raw.githubusercontent.com/heischichou/Covid-19-Data-Analysis/main/assets/Monthly%20Trend%20of%20Cumulative%20Case%20Outcomes/Monthly%20Trend%20of%20Cumulative%20Case%20Outcomes%20by%20Country%20-%20January.png"></img>
      <br>
      <!-- <img src="https://raw.githubusercontent.com/heischichou/Covid-19-Data-Analysis/main/assets/Monthly%20Trend%20of%20Cumulative%20Case%20Outcomes/Monthly%20Trend%20of%20Cumulative%20Case%20Outcomes%20by%20Country%20-%February.png"></img>
      <br> -->
      <img src="https://raw.githubusercontent.com/heischichou/Covid-19-Data-Analysis/main/assets/Monthly%20Trend%20of%20Cumulative%20Case%20Outcomes/Monthly%20Trend%20of%20Cumulative%20Case%20Outcomes%20by%20Country%20-%20March.png"></img>
      <br>
      <img src="https://raw.githubusercontent.com/heischichou/Covid-19-Data-Analysis/main/assets/Monthly%20Trend%20of%20Cumulative%20Case%20Outcomes/Monthly%20Trend%20of%20Cumulative%20Case%20Outcomes%20by%20Country%20-%20April.png"></img>
      <br>
      <img src="https://raw.githubusercontent.com/heischichou/Covid-19-Data-Analysis/main/assets/Monthly%20Trend%20of%20Cumulative%20Case%20Outcomes/Monthly%20Trend%20of%20Cumulative%20Case%20Outcomes%20by%20Country%20-%20May.png"></img>
      <br>
      <img src="https://raw.githubusercontent.com/heischichou/Covid-19-Data-Analysis/main/assets/Monthly%20Trend%20of%20Cumulative%20Case%20Outcomes/Monthly%20Trend%20of%20Cumulative%20Case%20Outcomes%20by%20Country%20-%20June.png"></img>
      <br>
      <img src="https://raw.githubusercontent.com/heischichou/Covid-19-Data-Analysis/main/assets/Monthly%20Trend%20of%20Cumulative%20Case%20Outcomes/Monthly%20Trend%20of%20Cumulative%20Case%20Outcomes%20by%20Country%20-%20July.png"></img>
      <br>
    </div>
  </div>
  <br>
  <p align="justify">&nbsp;&nbsp;Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
</details>

<details>
  <summary><strong>Geographical Inquiries</strong></summary>

  <details>
    <summary><strong>Case Outcomes by Country</strong></summary>
    <div>
      <div>
        <p><i>What are the top 5 countries with the highest death count?</i></p>
        <div align="center">
          <img src="https://raw.githubusercontent.com/heischichou/Covid-19-Data-Analysis/main/assets/Highest%20Death%20Count%20by%20Country/Highest%20Death%20Count%20by%20Country%20-%20January.png"></img>
          <br>
          <!-- <img src="https://raw.githubusercontent.com/heischichou/Covid-19-Data-Analysis/main/assets/Highest%20Death%20Count%20by%20Country/Highest%20Death%20Count%20by%20Country%20-%20February.png"></img>
          <br> -->
          <img src="https://raw.githubusercontent.com/heischichou/Covid-19-Data-Analysis/main/assets/Highest%20Death%20Count%20by%20Country/Highest%20Death%20Count%20by%20Country%20-%20March.png"></img>
          <br>
          <img src="https://raw.githubusercontent.com/heischichou/Covid-19-Data-Analysis/main/assets/Highest%20Death%20Count%20by%20Country/Highest%20Death%20Count%20by%20Country%20-%20April.png"></img>
          <br>
          <img src="https://raw.githubusercontent.com/heischichou/Covid-19-Data-Analysis/main/assets/Highest%20Death%20Count%20by%20Country/Highest%20Death%20Count%20by%20Country%20-%20May.png"></img>
          <br>
          <img src="https://raw.githubusercontent.com/heischichou/Covid-19-Data-Analysis/main/assets/Highest%20Death%20Count%20by%20Country/Highest%20Death%20Count%20by%20Country%20-%20June.png"></img>
          <br>
          <img src="https://raw.githubusercontent.com/heischichou/Covid-19-Data-Analysis/main/assets/Highest%20Death%20Count%20by%20Country/Highest%20Death%20Count%20by%20Country%20-%20July.png"></img>
          <br>
        </div>
      </div>
      <br>
      <p align="justify">&nbsp;&nbsp;Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
    </div>
    <br>
    <div>
      <div>
        <p><i>What are the top 5 countries with the highest recovery count?</i></p>
        <div align="center">
          <img src="https://raw.githubusercontent.com/heischichou/Covid-19-Data-Analysis/main/assets/Highest%20Recovery%20Count%20by%20Country/Highest%20Recovery%20Count%20by%20Country%20-%20January.png"></img>
          <br>
          <img src="https://raw.githubusercontent.com/heischichou/Covid-19-Data-Analysis/main/assets/Highest%20Recovery%20Count%20by%20Country/Highest%20Recovery%20Count%20by%20Country%20-%20February.png"></img>
          <br>
          <img src="https://raw.githubusercontent.com/heischichou/Covid-19-Data-Analysis/main/assets/Highest%20Recovery%20Count%20by%20Country/Highest%20Recovery%20Count%20by%20Country%20-%20March.png"></img>
          <br>
          <img src="https://raw.githubusercontent.com/heischichou/Covid-19-Data-Analysis/main/assets/Highest%20Recovery%20Count%20by%20Country/Highest%20Recovery%20Count%20by%20Country%20-%20April.png"></img>
          <br>
          <img src="https://raw.githubusercontent.com/heischichou/Covid-19-Data-Analysis/main/assets/Highest%20Recovery%20Count%20by%20Country/Highest%20Recovery%20Count%20by%20Country%20-%20May.png"></img>
          <br>
          <img src="https://raw.githubusercontent.com/heischichou/Covid-19-Data-Analysis/main/assets/Highest%20Recovery%20Count%20by%20Country/Highest%20Recovery%20Count%20by%20Country%20-%20June.png"></img>
          <br>
          <img src="https://raw.githubusercontent.com/heischichou/Covid-19-Data-Analysis/main/assets/Highest%20Recovery%20Count%20by%20Country/Highest%20Recovery%20Count%20by%20Country%20-%20July.png"></img>
          <br>
        </div>
      </div>
      <br>
      <p align="justify">&nbsp;&nbsp;Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
    </div>
  </details>

  <details>
    <summary><strong>Regional Percentages</strong></summary>
    <div>
      <div>
        <p><i>What are the percentages of cumulative death counts among the different WHO regions?</i></p>
        <div align="center">
          <img src="https://raw.githubusercontent.com/heischichou/Covid-19-Data-Analysis/main/assets/Regional%20Percentage%20of%20Cumulative%20Death%20Counts/Regional%20Percentage%20of%20Cumulative%20Death%20Counts%20-%20January.png"></img>
          <br>
          <!-- <img src="https://raw.githubusercontent.com/heischichou/Covid-19-Data-Analysis/main/assets/Highest%20Death%20Count%20by%20Country/Highest%20Death%20Count%20by%20Country%20-%20February.png"></img>
          <br> -->
          <img src="https://raw.githubusercontent.com/heischichou/Covid-19-Data-Analysis/main/assets/Regional%20Percentage%20of%20Cumulative%20Death%20Counts/Regional%20Percentage%20of%20Cumulative%20Death%20Counts%20-%20March.png"></img>
          <br>
          <img src="https://raw.githubusercontent.com/heischichou/Covid-19-Data-Analysis/main/assets/Regional%20Percentage%20of%20Cumulative%20Death%20Counts/Regional%20Percentage%20of%20Cumulative%20Death%20Counts%20-%20April.png"></img>
          <br>
          <img src="https://raw.githubusercontent.com/heischichou/Covid-19-Data-Analysis/main/assets/Regional%20Percentage%20of%20Cumulative%20Death%20Counts/Regional%20Percentage%20of%20Cumulative%20Death%20Counts%20-%20May.png"></img>
          <br>
          <img src="https://raw.githubusercontent.com/heischichou/Covid-19-Data-Analysis/main/assets/Regional%20Percentage%20of%20Cumulative%20Death%20Counts/Regional%20Percentage%20of%20Cumulative%20Death%20Counts%20-%20June.png"></img>
          <br>
          <img src="https://raw.githubusercontent.com/heischichou/Covid-19-Data-Analysis/main/assets/Regional%20Percentage%20of%20Cumulative%20Death%20Counts/Regional%20Percentage%20of%20Cumulative%20Death%20Counts%20-%20July.png"></img>
          <br>
        </div>
      </div>
      <br>
      <p align="justify">&nbsp;&nbsp;Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
    </div>
    <br>
    <div>
      <div>
        <p><i>What are the percentages of cumulative recovery counts among the different WHO regions?</i></p>
        <div align="center">
          <img src="https://raw.githubusercontent.com/heischichou/Covid-19-Data-Analysis/main/assets/Regional%20Percentage%20of%20Cumulative%20Recovery%20Counts/Regional%20Percentage%20of%20Cumulative%20Recovery%20Counts%20-%20January.png"></img>
          <br>
          <img src="https://raw.githubusercontent.com/heischichou/Covid-19-Data-Analysis/main/assets/Regional%20Percentage%20of%20Cumulative%20Recovery%20Counts/Regional%20Percentage%20of%20Cumulative%20Recovery%20Counts%20-%20February.png"></img>
          <br>
          <img src="https://raw.githubusercontent.com/heischichou/Covid-19-Data-Analysis/main/assets/Regional%20Percentage%20of%20Cumulative%20Recovery%20Counts/Regional%20Percentage%20of%20Cumulative%20Recovery%20Counts%20-%20March.png"></img>
          <br>
          <img src="https://raw.githubusercontent.com/heischichou/Covid-19-Data-Analysis/main/assets/Regional%20Percentage%20of%20Cumulative%20Recovery%20Counts/Regional%20Percentage%20of%20Cumulative%20Recovery%20Counts%20-%20April.png"></img>
          <br>
          <img src="https://raw.githubusercontent.com/heischichou/Covid-19-Data-Analysis/main/assets/Regional%20Percentage%20of%20Cumulative%20Recovery%20Counts/Regional%20Percentage%20of%20Cumulative%20Recovery%20Counts%20-%20May.png"></img>
          <br>
          <img src="https://raw.githubusercontent.com/heischichou/Covid-19-Data-Analysis/main/assets/Regional%20Percentage%20of%20Cumulative%20Recovery%20Counts/Regional%20Percentage%20of%20Cumulative%20Recovery%20Counts%20-%20June.png"></img>
          <br>
          <img src="https://raw.githubusercontent.com/heischichou/Covid-19-Data-Analysis/main/assets/Regional%20Percentage%20of%20Cumulative%20Recovery%20Counts/Regional%20Percentage%20of%20Cumulative%20Recovery%20Counts%20-%20July.png"></img>
          <br>
        </div>
      </div>
      <br>
      <p align="justify">&nbsp;&nbsp;Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
    </div>
  </details>
</details>

<details>
  <summary><strong>Other Results</strong></summary>
  <div>
    <p><i>Geographical locations in countries with recorded deaths</i></p>
    <div align="center">
      <img src="https://raw.githubusercontent.com/heischichou/Covid-19-Data-Analysis/main/assets/Locations%20in%20Countries%20with%20Recorded%20Deaths.png"></img>
    </div>
  </div>
</details>
