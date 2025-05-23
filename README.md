# HEIC to JPG Converter API

一个基于 Flask 的简单 API，用于将 HEIC 格式的图片转换为 JPG 格式。

## 功能

- 上传 HEIC 文件并转换为 JPG 格式。
- 提供下载已转换文件的接口。
- 提供直接查看已转换文件的接口。

## 演示网站

你可以访问以下链接体验在线转换功能：

[https://heic.tongchao.xyz](https://heic.tongchao.xyz)

## 运行项目

### 环境要求

- Python 3.8 或更高版本
- pip 包管理工具

### 安装依赖

```bash
pip install -r requirements.txt
```

### 启动服务

```bash
python trans.py
```

服务将运行在 `http://127.0.0.1:9876/`。

## Docker

```
docker build -t heic_trans_app .
docker run -d -p 9876:9876 --name heic_trans_container heic_trans_app
```

## 使用案例

以下是使用 `curl` 测试 API 的示例：

### 1. 上传 HEIC 文件并转换为 JPG

```bash
curl -X POST -F "file=@example.heic" http://127.0.0.1:9876/upload
```

**响应示例：**

```json
{
  "message": "File converted successfully",
  "url": "http://127.0.0.1:9876/download/1234567890abcdef.jpg"
}
```

### 2. 下载已转换的 JPG 文件

```bash
curl -O http://127.0.0.1:9876/download/1234567890abcdef.jpg
```

### 3. 查看已转换的 JPG 文件

```bash
curl http://127.0.0.1:9876/view/1234567890abcdef.jpg --output converted.jpg
```

## 文件结构

```
.
├── trans.py            # 主程序文件
├── templates/
│   └── index.html      # 前端页面
├── uploads/            # 上传和转换后的文件存储目录
├── requirements.txt    # 依赖文件
└── README.md           # 项目说明文档
```

## 注意事项

- 上传的文件必须为 `.heic` 格式，否则会返回错误。
- 转换后的文件会存储在 `uploads/` 目录中，请确保该目录有写入权限。

## 许可证
![Visited By](https://count.easyulife.com/get/@heic_trans?theme=gelbooru)

本项目采用 [MIT License](LICENSE)。
