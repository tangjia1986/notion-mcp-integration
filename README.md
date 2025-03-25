# Notion MCP 集成

本项目提供了 Notion API 的 Model Context Protocol (MCP) 实现，允许 AI 助手直接操作 Notion。

## 功能特性

- 页面操作
  - 创建页面
  - 更新页面
  - 查询页面
  - 删除页面
  
- 数据库操作
  - 创建数据库
  - 查询数据库
  - 添加/更新数据库条目
  
- 块操作
  - 添加内容块
  - 更新块内容
  - 删除块
  
- 搜索
  - 搜索页面
  - 搜索数据库

## 快速开始

1. 配置 Notion API
```bash
# 设置 Notion API 密钥
export NOTION_API_KEY=your_api_key
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 配置 MCP
将以下内容添加到你的 `mcp.json`:
```json
{
  "tools": {
    "notion": {
      "path": "./notion_mcp.py",
      "description": "Notion MCP integration"
    }
  }
}
```

## API 参考

### 页面操作

```python
# 创建页面
create_page(parent_id: str, title: str, content: dict)

# 更新页面
update_page(page_id: str, properties: dict)

# 获取页面
get_page(page_id: str)
```

### 数据库操作

```python
# 创建数据库
create_database(parent_id: str, title: str, properties: dict)

# 查询数据库
query_database(database_id: str, filter: dict = None)
```

## 示例

```python
# 创建新页面
response = notion.create_page(
    parent_id="your_parent_page_id",
    title="测试页面",
    content={
        "blocks": [
            {
                "type": "paragraph",
                "text": "这是一个测试页面"
            }
        ]
    }
)
```

## 贡献指南

1. Fork 本仓库
2. 创建特性分支
3. 提交变更
4. 发起 Pull Request

## 许可证

MIT License