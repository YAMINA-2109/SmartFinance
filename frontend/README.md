---

## 💼 SmartFinance Analyzer – Frontend App

**SmartFinance Analyzer** is a modern and responsive frontend built with **React**, **Tailwind CSS**, and **Chart.js**. It allows users to upload financial PDFs, visualize key insights, query documents in natural language, and explore dashboards interactively.

---

### 🌐 Features

- Upload and summarize financial PDF reports
- View executive summaries and extracted text
- Chat with the document (PDF QA chatbot with sources)
- Interactive dashboard with charts and financial KPIs
- Export CSV files for reporting or ETL pipelines

---

### 🧰 Tech Stack

- React 18+
- Vite
- Tailwind CSS
- Chart.js (Bar & Pie charts)
- Axios
- Lucide-react (icons)

---

### 📁 Project Structure

```bash
frontend/
│
├── src/
│   ├── components/        # UI components (Uploader, Viewer, Sidebar, Navbar, Cards, etc.)
│   ├── pages/             # Main pages (Home, Dashboard)
│   ├── context/           # React context for global state (e.g. TabContext)
│   ├── services/          # API calls and service logic (e.g. pdfService.js, dashboardService.js)
│   ├── style/             # CSS modules and custom styles (e.g. SummaryCard.module.css)
│   ├── utils/             # Utility functions (e.g. formatSummary.js)
│   ├── assets/            # Static assets (e.g. images, SVGs)
│   ├── hooks/             # Custom React hooks (if any)
│   ├── App.jsx            # Main app component and routing
│   ├── main.jsx           # App entry point
│   ├── App.css            # Global styles
│   └── index.css          # Tailwind or global CSS
│
├── public/
│   └── favicon, assets, logo...
│
├── package.json           # Project metadata and dependencies
├── package-lock.json      # Dependency lock file
├── vite.config.js         # Vite configuration
├── postcss.config.js      # PostCSS configuration
├── tailwind.config.js     # Tailwind CSS configuration
├── .env                   # Environment variables
├── README.md              # Frontend documentation
└── eslint.config.js       # ESLint configuration
```

---

### ⚙️ Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/YAMINA-2109/SmartFinance.git
cd frontend
```

2. **Install dependencies**

```bash
npm install
```

3. **Configure environment variables**

Create a `.env` fille in the root of your frontend:

```env
VITE_BACKEND_URL=http://localhost:8000

```

4. **Run the app**

```bash
npm run dev
```

---

### 🧩 Available Pages

| Route        | Description                           |
| ------------ | ------------------------------------- |
| `/`          | Home – Upload PDF and view summary    |
| `/dashboard` | Visual dashboard with charts & export |
| `/chat`      | Chatbot to ask questions about PDF    |

---

### 🖼️ Screenshot Previews

- Executive summary in bullet format
- Interactive bar and pie charts
- Natural language PDF Q\&A with source highlighting
- CSV export button

---

### ✅ To Do

- [ ] Add responsive mobile layout
- [ ] Improve chart tooltips and export images

---

### 🔐 Auth (future)

- [ ] JWT login system
- [ ] Role-based access (admin/user)

---

### 📣 Maintained by

**Yamina ATMAOUI**
