def parse_tags(s: str):
    # BUG: 标签约定为逗号分隔，这里却按空格拆分
    return [x.strip() for x in s.split(",") if x.strip()]

def pretty_print(tasks):
    print("ID  Title                   Tags                 Done Created At")
    for t in tasks:
        # BUG: 调用未定义函数 colour（NameError）
        status = "✓" if t.done else "x"
        tag_str = ",".join(t.tags)
        print(f"{t.id:<3} {t.title:<22} {tag_str:<20} {status} {t.created_at:%Y-%m-%d}")