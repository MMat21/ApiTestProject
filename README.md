# API 自动化测试项目

基于 Python + pytest + requests 构建的接口自动化测试项目。

## 项目功能

- 支持 GET、POST、PUT、DELETE 请求
- 封装统一 HTTP 请求层
- 使用 pytest 组织和执行测试用例
- 使用 pytest Fixture 实现依赖注入
- 使用 YAML 管理测试数据和环境配置
- 支持测试数据参数化
- 支持请求日志记录
- 支持异常处理和请求超时控制
- 支持生成 HTML 测试报告

## 技术栈

- Python 3.12
- pytest
- requests
- PyYAML
- pytest-html
- logging

## 项目结构

```text
ApiTestProject/
├── api/
│   └── posts.py              # API 接口层
│
├── common/
│   ├── request.py            # HTTP 请求封装
│   ├── logger.py             # 日志配置
│   └── read_data.py          # 测试数据读取
│
├── config/
│   ├── config.py             # 环境配置读取
│   ├── config.yaml           # 环境配置文件
│   └── api.py                # 接口路径配置
│
├── data/
│   ├── post_data.yaml        # POST 测试数据
│   └── update_data.yaml      # PUT 测试数据
│
├── testcase/
│   └── test_posts.py         # Posts 接口测试用例
│
├── conftest.py               # pytest Fixture 配置
├── pytest.ini                # pytest 配置
├── requirements.txt          # 项目依赖
├── .gitignore                # Git 忽略文件
└── README.md                 # 项目说明
```

## 环境要求

- Python 3.12+
- pip

## 安装依赖

```bash
pip install -r requirements.txt
```

## 执行测试

```bash
pytest
```

## 查看测试报告

测试执行完成后，会自动生成 HTML 测试报告：

```text
reports/report.html
```

## 核心设计

### 1. 分层设计

项目采用测试用例层、API 接口层和公共请求层进行分离：

```text
testcase
    ↓
api
    ↓
common
    ↓
HTTP 服务
```

- `testcase`：编写测试场景和断言
- `api`：封装具体业务接口
- `common`：封装 HTTP 请求、日志、数据读取等公共功能
- `config`：管理环境配置和接口地址
- `data`：管理测试数据

### 2. 统一 HTTP 请求封装

通过 `Request` 类统一封装 GET、POST、PUT、DELETE 请求，并集中处理：

- 请求参数
- Header
- 超时设置
- 响应数据解析
- 请求日志
- 网络异常

### 3. pytest Fixture 依赖注入

使用 pytest Fixture 管理 Request 和 API 对象。

测试用例通过参数获取 Fixture：

```python
def test_get_post(posts_api):
    result = posts_api.get_post(1)
```

降低测试用例与对象创建过程之间的耦合。

### 4. 测试数据与测试代码分离

使用 YAML 文件管理测试数据，并结合 `pytest.mark.parametrize` 实现多组数据测试：

```python
@pytest.mark.parametrize("data", read_json())
def test_post(data, posts_api):
    ...
```

## 测试用例

| 接口 | 测试场景 | 验证内容 |
|---|---|---|
| GET | 查询正常 Post | 状态码、返回 ID |
| GET | 查询不存在的 Post | 状态码 404 |
| GET | 异常 ID 参数化测试 | 0、-1、9999 均返回 404 |
| POST | 创建 Post | 状态码、ID、title、body |
| PUT | 更新 Post | 状态码、ID、title、body、userId |
| DELETE | 删除 Post | 状态码 |

### GET 正常场景

验证查询指定 Post 时接口能够正常返回数据：

```python
def test_get_post(posts_api):
    result = posts_api.get_post(1)

    assert result["status_code"] == 200
    assert result["data"]["id"] == 1
```

### GET 异常场景

使用参数化测试验证不存在的 Post ID：

```python
@pytest.mark.parametrize("post_id", [0, -1, 9999])
def test_get_post_invalid_id(posts_api, post_id):
    result = posts_api.get_post(post_id)

    assert result["status_code"] == 404
```

### POST 场景

通过参数化方式读取 YAML 测试数据，对创建 Post 接口进行多组数据测试：

```python
@pytest.mark.parametrize("data", read_json())
def test_post(data, posts_api):
    result = posts_api.create_post(data)

    assert result["status_code"] == 201
    assert result["data"]["id"] == data["expected_id"]
    assert result["data"]["title"] == data["title"]
    assert result["data"]["body"] == data["body"]
```

### PUT 场景

通过 YAML 测试数据验证 Post 更新功能：

```python
@pytest.mark.parametrize("data", read_update_data())
def test_update(data, posts_api):
    result = posts_api.update_post(1, data)

    assert result["status_code"] == 200
    assert result["data"]["id"] == 1
    assert result["data"]["title"] == data["title"]
    assert result["data"]["body"] == data["body"]
    assert result["data"]["userId"] == data["userId"]
```

### DELETE 场景

验证删除指定 Post 后接口返回正确的状态码：

```python
def test_delete(posts_api):
    result = posts_api.delete_post(1)

    assert result["status_code"] == 200
```

## 测试报告

项目使用 `pytest-html` 自动生成 HTML 测试报告。

执行：

```bash
pytest
```

报告生成路径：

```text
reports/report.html
```

测试报告包含：

- 测试执行结果
- 测试环境信息
- 测试用例详情
- 失败原因
- 测试日志

## CI 持续集成

项目使用 GitHub Actions 实现持续集成。

每次向 `main` 分支 push 代码或提交 Pull Request 时，GitHub Actions 会自动：

1. 拉取项目代码
2. 配置 Python 3.12 环境
3. 安装项目依赖
4. 执行 pytest 自动化测试
5. 生成 HTML 测试报告
6. 保存测试报告 Artifact

CI 流程：

```text
Git Push
   ↓
GitHub Actions
   ↓
Checkout Code
   ↓
Setup Python
   ↓
Install Dependencies
   ↓
Run pytest
   ↓
Generate HTML Report
   ↓
Upload Test Report
```
然后提交：

```bash
git add README.md
git commit -m "完善项目CI文档"
git push
```

## 项目亮点

- 基于 Python + pytest + requests 构建接口自动化测试框架
- 采用 API 层与 HTTP 请求层分离的设计
- 使用 pytest Fixture 实现依赖注入
- 使用 YAML 实现测试数据与代码分离
- 使用参数化测试覆盖多组测试数据和异常场景
- 统一处理请求日志、响应解析和网络异常
- 支持请求超时控制
- 支持自动生成 HTML 测试报告