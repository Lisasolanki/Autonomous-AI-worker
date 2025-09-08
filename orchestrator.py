def run_pipeline():
    # fetch data
    news_list = fetch_news("AI")
    market_text = fetch_market("AAPL")

    combined = "\n".join(news_list) + "\n" + str(market_text)

    # AI pipeline
    topics = extract_topics(combined)
    summary = summarize(combined)
    recs = generate_insights(summary, topics)

    # save to DB
    import sqlite3
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO insights (topics, summary, recommendations) VALUES (?, ?, ?)",
                (topics, summary, recs))
    conn.commit()
    conn.close()

    return {"topics": topics, "summary": summary, "recommendations": recs}
