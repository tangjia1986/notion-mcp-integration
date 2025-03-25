from notion_mcp import NotionMCP

def main():
    # 初始化 Notion MCP
    notion = NotionMCP()
    
    # 创建页面示例
    page = notion.create_page(
        parent_id="your_parent_page_id",  # 替换为实际的父页面 ID
        title="测试页面",
        content={
            "blocks": [
                {
                    "type": "paragraph",
                    "text": "这是一个测试页面的内容。"
                }
            ]
        }
    )
    print("创建的页面 ID:", page["id"])
    
    # 创建数据库示例
    database = notion.create_database(
        parent_id="your_parent_page_id",  # 替换为实际的父页面 ID
        title="测试数据库",
        properties={
            "名称": {
                "title": {}
            },
            "状态": {
                "select": {
                    "options": [
                        {"name": "待办", "color": "red"},
                        {"name": "进行中", "color": "yellow"},
                        {"name": "已完成", "color": "green"}
                    ]
                }
            },
            "优先级": {
                "number": {}
            }
        }
    )
    print("创建的数据库 ID:", database["id"])
    
    # 搜索示例
    results = notion.search(
        query="测试",
        filter={
            "property": "object",
            "value": "page"
        }
    )
    print("搜索结果:", results)

if __name__ == "__main__":
    main()