# Indeed Job Count Scraper

## Setup
1. Install python dependencies
```bash
pip install -r requirements.txt
```
2. Copy `config.json.sample` to a file called `config.json` and insert appropriate
   values
3. Run the script
```bash
python scraper.py
```
4. Optionally configure a cronjob in Linux or a scheduled task in windows to run at a
   given interval
```bash
# Example Crontab that runs every 6 hours
0 */6 * * * cd /opt/scraper && python scraper.py >/dev/null 2>&1
```

## Run roll-out.bat to start the autobots.py script.(old version)


## Additional file info

autobots.py = old script using excel to collect data
scraper.py = new script sending data to InfluxDB
influxdb.py = a backup/alternative version of scraper.py
roll-out.bat = for Zach to run on his computer - You can modify this to change the path.

## Overall it's a little sloppy in some places and I apologize for that, I'm new to this.
