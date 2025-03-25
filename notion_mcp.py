import os
from typing import Optional, Dict, List, Any
from notion_client import Client

class NotionMCP:
    def __init__(self):
        self.notion = Client(auth=os.environ.get("NOTION_API_KEY"))
        if not os.environ.get("NOTION_API_KEY"):
            raise ValueError("NOTION_API_KEY 环境变量未设置")

    def create_page(self, parent_id: str, title: str, content: Dict[str, Any]) -> Dict[str, Any]:
        """
        创建新的 Notion 页面
        
        Args:
            parent_id: 父页面或数据库的 ID
            title: 页面标题
            content: 页面内容配置
        
        Returns:
            创建的页面信息
        """
        page_data = {
            "parent": {"page_id": parent_id},
            "properties": {
                "title": {
                    "title": [
                        {
                            "text": {
                                "content": title
                            }
                        }
                    ]
                }
            }
        }
        
        if "blocks" in content:
            page_data["children"] = self._convert_blocks(content["blocks"])
            
        return self.notion.pages.create(**page_data)

    def update_page(self, page_id: str, properties: Dict[str, Any]) -> Dict[str, Any]:
        """
        更新页面属性
        
        Args:
            page_id: 页面 ID
            properties: 要更新的属性
            
        Returns:
            更新后的页面信息
        """
        return self.notion.pages.update(page_id=page_id, properties=properties)

    def get_page(self, page_id: str) -> Dict[str, Any]:
        """
        获取页面信息
        
        Args:
            page_id: 页面 ID
            
        Returns:
            页面详细信息
        """
        return self.notion.pages.retrieve(page_id=page_id)

    def create_database(self, parent_id: str, title: str, properties: Dict[str, Any]) -> Dict[str, Any]:
        """
        创建新的数据库
        
        Args:
            parent_id: 父页面 ID
            title: 数据库标题
            properties: 数据库属性配置
            
        Returns:
            创建的数据库信息
        """
        return self.notion.databases.create(
            parent={"page_id": parent_id},
            title=[{"text": {"content": title}}],
            properties=properties
        )

    def query_database(self, database_id: str, filter: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        查询数据库
        
        Args:
            database_id: 数据库 ID
            filter: 过滤条件
            
        Returns:
            查询结果
        """
        return self.notion.databases.query(
            database_id=database_id,
            filter=filter
        )

    def append_block(self, block_id: str, children: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        添加内容块
        
        Args:
            block_id: 块 ID
            children: 子块配置
            
        Returns:
            添加的块信息
        """
        return self.notion.blocks.children.append(
            block_id=block_id,
            children=children
        )

    def update_block(self, block_id: str, content: Dict[str, Any]) -> Dict[str, Any]:
        """
        更新块内容
        
        Args:
            block_id: 块 ID
            content: 新的内容
            
        Returns:
            更新后的块信息
        """
        return self.notion.blocks.update(block_id=block_id, **content)

    def delete_block(self, block_id: str) -> Dict[str, Any]:
        """
        删除块
        
        Args:
            block_id: 块 ID
            
        Returns:
            删除操作结果
        """
        return self.notion.blocks.delete(block_id=block_id)

    def search(self, query: str, filter: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        搜索 Notion
        
        Args:
            query: 搜索关键词
            filter: 过滤条件
            
        Returns:
            搜索结果
        """
        return self.notion.search(
            query=query,
            filter=filter
        )

    def _convert_blocks(self, blocks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        转换块配置为 Notion API 格式
        
        Args:
            blocks: 块配置列表
            
        Returns:
            转换后的块配置
        """
        converted_blocks = []
        for block in blocks:
            if block["type"] == "paragraph":
                converted_blocks.append({
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": [
                            {
                                "type": "text",
                                "text": {
                                    "content": block["text"]
                                }
                            }
                        ]
                    }
                })
            # 可以添加其他类型的块转换
        return converted_blocks

# MCP 工具函数
def create_page(parent_id: str, title: str, content: Dict[str, Any]) -> Dict[str, Any]:
    """创建页面的 MCP 工具函数"""
    notion = NotionMCP()
    return notion.create_page(parent_id, title, content)

def update_page(page_id: str, properties: Dict[str, Any]) -> Dict[str, Any]:
    """更新页面的 MCP 工具函数"""
    notion = NotionMCP()
    return notion.update_page(page_id, properties)

def get_page(page_id: str) -> Dict[str, Any]:
    """获取页面的 MCP 工具函数"""
    notion = NotionMCP()
    return notion.get_page(page_id)

def create_database(parent_id: str, title: str, properties: Dict[str, Any]) -> Dict[str, Any]:
    """创建数据库的 MCP 工具函数"""
    notion = NotionMCP()
    return notion.create_database(parent_id, title, properties)

def query_database(database_id: str, filter: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """查询数据库的 MCP 工具函数"""
    notion = NotionMCP()
    return notion.query_database(database_id, filter)

def search(query: str, filter: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """搜索的 MCP 工具函数"""
    notion = NotionMCP()
    return notion.search(query, filter)