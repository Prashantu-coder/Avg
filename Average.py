import pandas as pd

sheet_id = "1wu5nOv1xkv1BZpcGRC63ZDaWUUSiLiZ3WuxuBesXLEY"
gid = "992072017"

def load_google_sheet(sheet_id, gid):
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}"
    df= pd.read_csv(url)
    return df

data = load_google_sheet(sheet_id, gid)

print(data.head())

html_table = data.to_html(index=False)

with open("sheet_data.html", "w", encoding="utf-8") as f:
    f.write("<html><head><title>Google Sheet Data</title></head><body>")
    f.write("<h2>Imported Google Sheet</h2>")
    f.write(html_table)
    f.write("</body></html>")