# update_google_links.py

input_file = "748_final_all_companies.txt"
output_file = "google_links_companiess.txt"

# Read already processed URLs (we'll extract queries from them)
existing_queries = set()
try:
    with open(output_file, "r", encoding="utf-8") as f:
        for line in f:
            if "search?q=" in line:
                query_part = line.strip().split("search?q=")[-1]
                existing_queries.add(query_part.lower())
except FileNotFoundError:
    # First time run: file doesn't exist
    pass

# Process new company names
with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "a", encoding="utf-8") as outfile:
    for line in infile:
        company = line.strip()
        if company:
            query = company.replace(" ", "+")
            if query.lower() not in existing_queries:
                url = f"https://www.google.com/search?q={query}"
                outfile.write(url + "\n")
                print(f"✅ Added: {url}")
            else:
                print(f"⏩ Skipped (already exists): {company}")

print("🎉 Done updating google_links.txt")
