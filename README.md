# AutoPoster - 自动化内容发布工具

<div align="center">

**让内容创作和发布自动化**

一个开源的自动化内容发布工具，支持多平台、定时发布、AI 辅助创作。

[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![GitHub stars](https://img.shields.io/github/stars/PHclaw/autoposter?style=social)](https://github.com/PHclaw/autoposter)

</div>

---

## ✨ 特性

- 📱 **多平台发布** - Twitter、LinkedIn、知乎、公众号等
- 🤖 **AI 辅助创作** - 基于 LLM 生成文案、配图
- ⏰ **定时发布** - 智能排程，最佳发布时间
- 📊 **数据统计** - 发布效果追踪与分析
- 🔄 **工作流自动化** - 自动抓取、改编、发布
- 🔓 **完全开源** - MIT 协议，无供应商锁定

## 🏗️ 技术栈

### 后端
- FastAPI + SQLAlchemy
- PostgreSQL / SQLite
- Redis (任务队列)
- OpenAI / Anthropic / DeepSeek (LLM)

### 前端
- React 18 + TypeScript
- Tailwind CSS
- Vite

## 🚀 快速开始

### 后端

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate  # Windows
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload --port 8000
```

### 前端

```bash
cd frontend
npm install
npm run dev
```

## 📁 项目结构

```
autoposter/
├── backend/
│   ├── app/
│   │   ├── api/          # API 路由
│   │   ├── core/         # 核心配置
│   │   ├── models/       # 数据模型
│   │   ├── services/     # 业务服务
│   │   └── schedulers/   # 定时任务
│   └── requirements.txt
├── frontend/
│   └── src/
│       └── App.tsx
└── README.md
```

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 License

MIT License