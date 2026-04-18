import os

from serpapi import SerpApiClient


def search(query: str):
    print(f'正在执行搜索网页: {query}')
    try:
        api_key = os.getenv("SERPAPI_API_KEY")
        if api_key is None:
            print('api未配置')
            return "API未配置"

        params = {
            'q': query,
            'api_key': api_key,  # 建议用下划线命名 api_key
            'engine': 'google',
            'gl': 'us',  # 建议改成 us (美国)，因为 Google Search 的 cn 地区结果有时为空
            'hl': 'zh-cn'  # 保持中文搜索结果
        }
        client = SerpApiClient(params)
        results = client.get_dict()

        # 1. 检查 API 是否返回了错误信息（比如额度不足、Key无效）
        if "error" in results:
            print(f"❌ SerpApi 返回错误: {results['error']}")
            return f"搜索服务报错: {results['error']}"

        # 2. 智能搜索解析逻辑
        if "answer_box_list" in results:
            return "\n".join([str(item) for item in results["answer_box_list"]])

        if "answer_box" in results and "answer" in results["answer_box"]:
            return results["answer_box"]["answer"]

        if "knowledge_graph" in results and "description" in results["knowledge_graph"]:
            return results["knowledge_graph"]["description"]

        if "organic_results" in results and results["organic_results"]:
            snippets = [
                f"[{i + 1}] {res.get('title', '')}\n{res.get('snippet', '')}"
                for i, res in enumerate(results["organic_results"][:3])
            ]
            return "\n\n".join(snippets)

        # 3. 兜底打印：如果什么都没匹配上，打印出 SerpApi 到底返回了什么字段，方便调试
        print(f"⚠️ 未命中任何解析规则，当前返回的数据字段包含: {list(results.keys())}")
        return f"对不起，没有找到关于 '{query}' 的信息。"

    except Exception as e:
        return f"搜索时发生错误: {e}"