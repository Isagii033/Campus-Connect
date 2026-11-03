import os
import sys
from fpdf import FPDF
from fpdf.enums import XPos, YPos

class CampusConnectPDF(FPDF):
    def __init__(self):
        super().__init__(orientation="P", unit="mm", format="A4")
        self.set_auto_page_break(auto=True, margin=18)
        self.set_margins(left=18, top=16, right=18)
        self.is_cover = True

        # Register Unicode TrueType Fonts from Windows Fonts
        font_dir = "C:/Windows/Fonts"
        self.add_font("ArialUni", "", os.path.join(font_dir, "arial.ttf"))
        self.add_font("ArialUni", "B", os.path.join(font_dir, "arialbd.ttf"))
        self.add_font("ArialUni", "I", os.path.join(font_dir, "ariali.ttf"))
        self.add_font("ArialUni", "BI", os.path.join(font_dir, "arialbi.ttf"))

    def header(self):
        if not self.is_cover:
            self.set_font("ArialUni", "B", 8)
            self.set_text_color(110, 110, 130)
            self.cell(0, 6, "CampusConnect - Academic Project Technical Report & Viva Examination Guide", 
                      border="B", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="L")
            self.ln(4)

    def footer(self):
        if not self.is_cover:
            self.set_y(-14)
            self.set_font("ArialUni", "I", 8)
            self.set_text_color(130, 130, 150)
            self.cell(0, 8, f"CampusConnect Project Report | Page {self.page_no()} of {{nb}}", align="C")

    def print_cover(self):
        self.is_cover = True
        self.add_page()
        
        # Decorative top bar
        self.set_fill_color(79, 70, 229) # Indigo #4F46E5
        self.rect(0, 0, 210, 10, style="F")
        
        self.ln(22)
        # Badge
        self.set_fill_color(238, 242, 255) # Soft Lavender
        self.set_text_color(79, 70, 229)
        self.set_font("ArialUni", "B", 9.5)
        self.cell(75, 7.5, " COLLEGE PROJECT & VIVA REPORT ", align="C", fill=True, 
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(7)
        
        # Main Title
        self.set_text_color(31, 41, 55)
        self.set_font("ArialUni", "B", 24)
        self.multi_cell(0, 10.5, "CampusConnect: Peer-to-Peer Student Assistance & Skills Platform")
        self.ln(3)
        
        # Subtitle
        self.set_text_color(100, 116, 139)
        self.set_font("ArialUni", "", 12)
        self.multi_cell(0, 6.5, "Complete Technical Documentation, Engineering Rationale for Technologies Used, System Architecture, Business Validation Engine, and 20+ University Viva Questions & Answers.")
        self.ln(10)
        
        # Metadata Card
        self.set_fill_color(248, 250, 252)
        self.set_draw_color(199, 210, 254)
        card_y = self.get_y()
        self.rect(18, card_y, 174, 56, style="FD")
        
        self.set_xy(23, card_y + 4.5)
        self.set_text_color(67, 56, 202)
        self.set_font("ArialUni", "B", 10.5)
        self.cell(0, 5.5, "EXECUTIVE TECHNICAL SPECIFICATIONS", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        
        specs = [
            ("Project Name:", "CampusConnect (Single-File Autonomous Architecture)"),
            ("Application Type:", "Single-Page Web Application (SPA)"),
            ("Frontend Core:", "Semantic HTML5, Advanced Modern CSS3, Vanilla ES6+ JavaScript"),
            ("UI & Design System:", "Tailwind CSS (via CDN) + FontAwesome 6 + Inter Font"),
            ("State & Database:", "Client-Side Reactive Engine simulating NoSQL Collections via LocalStorage"),
            ("Security & Access:", "Credential-based Authentication, Session State, Role Persona Toggle"),
            ("Key Innovations:", "4-Step Wizard, Dynamic Payout Calculator, Dark Mode, Zero-Build"),
        ]
        
        for label, val in specs:
            self.set_x(23)
            self.set_font("ArialUni", "B", 8.8)
            self.set_text_color(79, 70, 229)
            self.cell(38, 5.5, label)
            self.set_font("ArialUni", "", 8.8)
            self.set_text_color(55, 65, 81)
            self.cell(0, 5.5, val, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            
        self.set_y(card_y + 64)
        
        # Additional Project Details Box
        self.set_fill_color(240, 253, 244) # Light emerald
        self.set_draw_color(187, 247, 208)
        self.rect(18, self.get_y(), 174, 28, style="FD")
        
        self.set_xy(23, self.get_y() + 3.5)
        self.set_text_color(21, 128, 61)
        self.set_font("ArialUni", "B", 9.5)
        self.cell(0, 5, "ACADEMIC & EVALUATION READY", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        
        self.set_x(23)
        self.set_font("ArialUni", "", 8.5)
        self.set_text_color(55, 65, 81)
        self.multi_cell(164, 4.5, "This documentation has been formatted to directly prepare students for university project presentations, internal/external viva examinations, and software engineering interviews. It details architectural trade-offs, security considerations, and future cloud scaling.")
        
        self.ln(8)
        self.set_font("ArialUni", "I", 8.5)
        self.set_text_color(120, 130, 150)
        self.cell(0, 5, "Source Code Repository: https://github.com/Isagii033/Campus-Connect.git", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.cell(0, 5, "Deployment Model: Autonomous zero-dependency browser-executable runtime", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        
        self.is_cover = False

    def section_header(self, title):
        self.ln(5)
        curr_y = self.get_y()
        if curr_y > 250:
            self.add_page()
            curr_y = self.get_y()
            
        self.set_fill_color(238, 242, 255)
        self.set_draw_color(79, 70, 229)
        self.rect(18, curr_y, 174, 8.5, style="F")
        self.rect(18, curr_y, 3, 8.5, style="F")
        
        self.set_xy(23, curr_y + 1.6)
        self.set_font("ArialUni", "B", 11)
        self.set_text_color(67, 56, 202)
        self.cell(0, 5.5, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(2.5)

    def sub_header(self, title):
        self.ln(2)
        self.set_font("ArialUni", "B", 10)
        self.set_text_color(31, 41, 55)
        self.cell(0, 5.5, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(1)

    def paragraph(self, text):
        self.set_font("ArialUni", "", 9)
        self.set_text_color(55, 65, 81)
        self.multi_cell(0, 4.8, text)
        self.ln(2)

    def bullet(self, title, text):
        self.set_font("ArialUni", "B", 9)
        self.set_text_color(79, 70, 229)
        self.cell(5, 4.8, ">")
        self.cell(self.get_string_width(title + ": ") + 1, 4.8, title + ": ")
        self.set_font("ArialUni", "", 9)
        self.set_text_color(55, 65, 81)
        self.multi_cell(0, 4.8, text)
        self.ln(1.5)

    def tech_box(self, tech_name, category, why_chosen, key_benefit):
        curr_y = self.get_y()
        if curr_y > 240:
            self.add_page()
            curr_y = self.get_y()
            
        self.set_fill_color(249, 250, 251)
        self.set_draw_color(229, 231, 235)
        self.rect(18, curr_y, 174, 27, style="FD")
        
        self.set_fill_color(79, 70, 229)
        self.rect(18, curr_y, 3, 27, style="F")
        
        self.set_xy(23, curr_y + 2)
        self.set_font("ArialUni", "B", 9.5)
        self.set_text_color(31, 41, 55)
        self.cell(70, 5, tech_name)
        
        self.set_font("ArialUni", "I", 8)
        self.set_text_color(100, 116, 139)
        self.cell(0, 5, f"Category: {category}", align="R", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        
        self.set_xy(23, curr_y + 7.5)
        self.set_font("ArialUni", "B", 8.2)
        self.set_text_color(79, 70, 229)
        self.cell(17, 4.2, "Why Used:")
        self.set_font("ArialUni", "", 8.2)
        self.set_text_color(55, 65, 81)
        self.multi_cell(152, 4.2, why_chosen)
        
        self.set_xy(23, curr_y + 17)
        self.set_font("ArialUni", "B", 8.2)
        self.set_text_color(16, 185, 129)
        self.cell(19, 4.2, "Key Benefit:")
        self.set_font("ArialUni", "", 8.2)
        self.set_text_color(55, 65, 81)
        self.multi_cell(150, 4.2, key_benefit)
        
        self.set_y(curr_y + 30)

    def qa_item(self, q_num, question, answer, category_tag="General"):
        if self.get_y() > 235:
            self.add_page()
            
        curr_y = self.get_y()
        self.set_fill_color(241, 245, 249)
        self.set_draw_color(226, 232, 240)
        self.rect(18, curr_y, 174, 7.5, style="F")
        
        self.set_xy(21, curr_y + 1.2)
        self.set_font("ArialUni", "B", 8.8)
        self.set_text_color(79, 70, 229)
        self.cell(12, 5, f"Q{q_num}:")
        
        self.set_text_color(31, 41, 55)
        self.set_font("ArialUni", "B", 8.8)
        self.cell(130, 5, question)
        
        self.set_font("ArialUni", "I", 7.5)
        self.set_text_color(100, 116, 139)
        self.cell(0, 5, f"[{category_tag}]", align="R", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        
        self.ln(1.8)
        self.set_x(21)
        self.set_font("ArialUni", "B", 8.2)
        self.set_text_color(16, 185, 129)
        self.cell(12, 4.5, "Answer:")
        
        self.set_font("ArialUni", "", 8.2)
        self.set_text_color(55, 65, 81)
        self.multi_cell(158, 4.5, answer)
        self.ln(3.5)

def generate_full_report(output_path):
    pdf = CampusConnectPDF()
    pdf.alias_nb_pages()
    
    # Page 1: Cover
    pdf.print_cover()
    
    # Page 2: Problem Statement & Architecture
    pdf.add_page()
    pdf.section_header("1. PROBLEM STATEMENT & ACADEMIC RELEVANCE")
    pdf.paragraph(
        "On college campuses, students frequently experience urgent micro-needs such as finding urgent tutoring "
        "for mathematics modules, requesting a peer with a DSLR camera for college fest photography, seeking slide "
        "deck design assistance for pitch competitions, or arranging immediate carpools/rideshares. At the same "
        "time, skilled students seek legitimate on-campus avenues to monetize their technical, creative, or academic "
        "talents. Commercial freelancing platforms (Upwork, Fiverr) fail at the campus level due to high minimum "
        "payout thresholds, steep platform fees (up to 20%), payment delays, and total absence of campus physical "
        "context. CampusConnect solves this gap with a lightweight, peer-to-peer micro-collaboration web platform."
    )
    
    pdf.section_header("2. SYSTEM ARCHITECTURE & RUNTIME FLOW")
    pdf.paragraph(
        "CampusConnect is architected as an autonomous Single-Page Application (SPA). The full UI routing, form "
        "processing, transactional state transitions, and persistent storage execute directly in the browser runtime. "
        "This completely eliminates client-server latency, allows instantaneous demonstration, and simulates cloud "
        "database interactions without complex server deployments."
    )
    
    pdf.bullet("Client-Side Routing Engine", "Monitors navigation requests and toggles visual page containers (Home, Browse, Post Wizard, Dashboard, Profile, Auth) without invoking browser reloads.")
    pdf.bullet("Document Data Store", "A simulated NoSQL schema maintained in window.localStorage across four collections: 'cc_users', 'cc_requests', 'cc_reviews', and 'cc_notifications'.")
    pdf.bullet("Dual Identity Engine", "Enables seamless evaluation of multi-user transactional workflows by allowing instant switching between Rahul Sharma (Requester) and Ananya Roy (Provider).")
    pdf.bullet("Reactive UI Pipeline", "Data mutations immediately update the DOM, dispatch visual toast notifications, update the notification counter badge, and re-render marketplace filters.")
    
    # Page 3: Technologies Used and Why
    pdf.add_page()
    pdf.section_header("3. TECHNOLOGIES EMPLOYED & ENGINEERING JUSTIFICATION")
    pdf.paragraph(
        "Each architectural component and library in CampusConnect was chosen intentionally based on performance, "
        "maintainability, developer experience, and academic clarity:"
    )
    
    pdf.tech_box(
        "Vanilla JavaScript (ES6+ Standards)",
        "Core Logic & State Management",
        "Used modern ES6+ features (arrow functions, template literals, destructuring, array filter/map/reduce). Avoids bulky framework overhead (React/Angular) and build tools.",
        "Instant zero-compilation execution, 100% portable on any web browser, zero dependency vulnerabilities."
    )
    
    pdf.tech_box(
        "HTML5 Semantic Architecture",
        "Document & Accessibility Foundation",
        "Employs semantic container elements (<header>, <main>, <nav>, <section>) to enforce structured DOM trees, enhance screen-reader accessibility, and streamline layout logic.",
        "Guarantees standard compliance, clean separation of concerns, and reliable cross-device rendering."
    )
    
    pdf.tech_box(
        "Tailwind CSS (Utility-First via CDN)",
        "Styling & Responsive Layout",
        "Enables rapid, cohesive design using pre-compiled atomic classes (e.g., flex, grid, rounded-2xl, shadow-lg). Eliminates writing thousands of lines of redundant CSS.",
        "Provides consistent color palettes, responsive design breakpoints, and modern aesthetics."
    )
    
    pdf.tech_box(
        "HTML5 LocalStorage API",
        "Simulated NoSQL Database",
        "Stores JSON serialized document collections to simulate cloud NoSQL document stores (such as MongoDB or Firebase Firestore).",
        "Persistent data across browser sessions and page refreshes with zero backend infrastructure requirements."
    )
    
    pdf.tech_box(
        "Custom Modern CSS3 Animations",
        "Micro-Interactions & Aesthetics",
        "Implements backdrop-filter glassmorphism, spring cubic-bezier transitions, floating ambient background gradients, and card elevation hover transforms.",
        "Produces a visually appealing, production-grade 60 FPS startup user experience."
    )
    
    pdf.tech_box(
        "FontAwesome 6.5 Vector Iconography",
        "Visual Language & UX Semantics",
        "Integrates high-resolution vector icons for service categories, star ratings, navigation links, and notification indicators.",
        "Sharp scaling on high-DPI screens, clear cognitive cues, and intuitive user comprehension."
    )
    
    # Page 4: Deep Dive into Modules
    pdf.add_page()
    pdf.section_header("4. MODULE-LEVEL FUNCTIONAL BREAKDOWN")
    
    pdf.sub_header("4.1 Authentication & Session Management")
    pdf.paragraph(
        "CampusConnect features a complete authentication pipeline. Users can register with their name, department, "
        "year, email, password, and skills. Passwords require a minimum 6-character length and confirmation verification. "
        "For quick evaluations, two pre-configured demo student accounts (Rahul Sharma and Ananya Roy) can be logged in "
        "with a single click. Sessions persist in localStorage until explicit logout."
    )
    
    pdf.sub_header("4.2 Multi-Persona Identity Engine")
    pdf.paragraph(
        "In peer-to-peer platforms, evaluating the interaction between a buyer and seller typically requires two laptops "
        "or separate incognito windows. CampusConnect solves this with an instant account switcher in the top bar. "
        "Switching personas dynamically updates the active session, header avatar, profile views, and permissions."
    )
    
    pdf.sub_header("4.3 4-Step Guided Request Posting Wizard")
    pdf.paragraph(
        "Rather than presenting users with an intimidating single-page form, the wizard uses cognitive chunking:\n"
        "- Step 1 (Category): Visual radio cards for Photography, Notes, Presentations, Teammates, Transport, Other.\n"
        "- Step 2 (Details): Title, comprehensive description, and special equipment/skill requirements.\n"
        "- Step 3 (Logistics): Targeted campus location (Auditorium, Library, Labs, Gates) and date/time picker.\n"
        "- Step 4 (Economics): Budget in Rupees with a live commission calculation (10% platform fee, 90% provider payout)."
    )
    
    pdf.sub_header("4.4 Strict Business Logic & Integrity Validation")
    pdf.paragraph(
        "The system enforces critical business rules directly within the transaction pipeline:\n"
        "- Anti-Self-Acceptance: Users cannot accept their own requests (prevents fraudulent review/completion farming).\n"
        "- Status Locking: Once accepted, requests transition from 'OPEN' to 'ACCEPTED' and become locked from further bids.\n"
        "- Dual-Handshake Completion: The provider marks the task complete ('IN_PROGRESS'), and the requester must confirm completion to finalize the record and unlock provider payouts."
    )
    
    pdf.sub_header("4.5 Interactive Star Rating & Review Engine")
    pdf.paragraph(
        "Upon completion confirmation, an interactive 1-to-5 star rating modal opens with review text input. Upon submission, "
        "all historical reviews for the provider are aggregated, and the user's cumulative average rating is recalculated "
        "and displayed across their public profile."
    )
    
    pdf.sub_header("4.6 Dark Mode & Accessibility Engine")
    pdf.paragraph(
        "A dedicated dark mode toggle supports late-night campus studying. It dynamically toggles the '.dark' CSS class on "
        "the document body, switching to a high-contrast deep navy/indigo palette (#0F1117 / #1A1C2E). Theme preferences "
        "are saved and restored on reload."
    )
    
    # Page 5: College Viva Questions - Part 1
    pdf.add_page()
    pdf.section_header("5. COLLEGE VIVA & TECHNICAL INTERVIEW Q&A")
    pdf.paragraph(
        "The following 22 questions and detailed answers cover system architecture, frontend engineering, database design, "
        "security, and scalability. They are structured to prepare students for project presentations and technical evaluations."
    )
    
    pdf.sub_header("Category 1: Software Architecture & Design Principles")
    
    pdf.qa_item(
        1,
        "What software architecture does CampusConnect follow?",
        "CampusConnect implements a Single-Page Application (SPA) architecture combined with a Model-View-Controller (MVC) "
        "inspired client-side pattern. The Model corresponds to the JSON document collections in LocalStorage; the Controller "
        "consists of event dispatchers and state mutation functions (e.g., acceptRequest, submitRating); and the View consists "
        "of dynamic template-rendering functions (e.g., renderBrowse, renderDashboard) that inject sanitized HTML into the DOM.",
        "Architecture"
    )
    
    pdf.qa_item(
        2,
        "Why was an SPA chosen instead of a traditional Multi-Page Application (MPA)?",
        "In an MPA, every page navigation triggers a full HTTP request, server response, and complete DOM re-render, creating "
        "visible page flashes and latency. An SPA loads assets once on initial boot and swaps component views in-memory using JavaScript. "
        "This delivers smooth desktop-like performance, preserves client-side state across tabs, and eliminates server hosting overhead.",
        "Architecture"
    )
    
    pdf.qa_item(
        3,
        "Why build this with Vanilla JavaScript rather than React, Vue, or Angular?",
        "Three key engineering reasons: (1) Performance: React incurs a ~140KB bundle size and virtual DOM reconciliation overhead; "
        "Vanilla JS runs with zero runtime overhead. (2) Zero-Build Portability: The entire application runs directly in any browser "
        "without requiring Node.js, Webpack, Vite, or Babel. (3) Mastery of Fundamentals: Demonstrates deep proficiency in native DOM APIs, "
        "event propagation, asynchronous programming, and closures without relying on external framework abstractions.",
        "Frontend"
    )
    
    pdf.qa_item(
        4,
        "How is data persisted without a traditional backend database server?",
        "We utilize the browser's HTML5 LocalStorage API as an embedded NoSQL document store. Four separate collections are maintained: "
        "'cc_users', 'cc_requests', 'cc_reviews', and 'cc_notifications'. Atomic helper functions (getRequests(), saveRequests()) "
        "serialize and deserialize JavaScript objects to and from JSON strings. Seed data is loaded automatically on initial boot if the storage is empty.",
        "Data Storage"
    )
    
    pdf.qa_item(
        5,
        "What are the technical limitations of LocalStorage and how would you resolve them?",
        "LocalStorage is synchronous (blocking the main thread on heavy I/O), limited to ~5MB per origin, lacks native indexing or complex "
        "query capabilities, and is accessible to any script running on the domain (making it vulnerable to XSS attacks). For production, we would "
        "migrate to a cloud REST or GraphQL API backed by MongoDB or PostgreSQL, storing authentication tokens in secure HTTP-only cookies.",
        "Database"
    )
    
    # Page 6: Viva Questions - Part 2
    pdf.add_page()
    pdf.sub_header("Category 2: Business Logic, State Verification, & Economics")
    
    pdf.qa_item(
        6,
        "How does the application prevent fraudulent self-acceptance of requests?",
        "In acceptRequest(id), the active user's ID is compared against req.requesterId. If req.requesterId === activeUser.id, execution is "
        "halted immediately with an error toast ('You cannot accept your own request!'). Additionally, the UI conditionally replaces the "
        "'Accept' button with an informative banner ('You posted this request') whenever the author views their own post.",
        "Business Logic"
    )
    
    pdf.qa_item(
        7,
        "Explain the lifecycle states of a request from creation to completion.",
        "A request transitions through four distinct states: (1) OPEN: Request is published and visible on the marketplace. "
        "(2) ACCEPTED: A provider claims the task, locking the request. (3) IN_PROGRESS: The provider finishes the work and marks the task complete. "
        "(4) COMPLETED: The original requester confirms completion, releasing payout credits and triggering the star rating modal.",
        "State Machine"
    )
    
    pdf.qa_item(
        8,
        "How is the 10% platform commission calculated and why is it important?",
        "In Step 4 of the wizard, an oninput handler triggers updateBudgetPreview(). For budget B: Platform Fee = round(B * 0.10), "
        "Provider Payout = round(B * 0.90). Transparently displaying fee breakdowns upfront builds user trust, prevents payment disputes, "
        "and illustrates the real monetization model used by commercial peer-to-peer marketplaces (e.g., TaskRabbit, Uber).",
        "Economics"
    )
    
    pdf.qa_item(
        9,
        "How is the provider's star rating dynamically recalculated?",
        "When submitRating(requestId) executes, a new review record is appended to 'cc_reviews'. The function queries all reviews matching "
        "review.providerId === req.providerId, calculates the arithmetic mean: sum(ratings) / count(reviews), rounds the result to 1 decimal place, "
        "and updates the provider's rating property in 'cc_users'.",
        "Algorithms"
    )
    
    pdf.qa_item(
        10,
        "How does the multi-criteria search and filtering algorithm work?",
        "renderBrowse() extracts values from four filter inputs: keyword search, category, budget bracket, and status. It applies JavaScript's "
        "Array.prototype.filter() with multiple chained predicates: case-insensitive substring matching on title/description, category equality, "
        "budget range checks, and status equality. Finally, Array.prototype.sort() orders matching requests by createdAt descending.",
        "Data Filtering"
    )
    
    pdf.qa_item(
        11,
        "How are real-time notifications dispatched without WebSockets?",
        "State-modifying functions trigger addNotification(userId, title, message). This prepends a new notification object into 'cc_notifications', "
        "persists the collection, and calls updateNotifBadge() to update the unread count badge on the bell icon. A slide-out drawer lets users "
        "browse historical alerts and mark all as read.",
        "Events"
    )

    # Page 7: Viva Questions - Part 3
    pdf.add_page()
    pdf.sub_header("Category 3: UI/UX, CSS Architecture, & Accessibility")
    
    pdf.qa_item(
        12,
        "How is Dark Mode implemented and how does it persist?",
        "Dark mode utilizes CSS class toggling on the <body> tag. Clicking the toggle executes document.body.classList.toggle('dark') and "
        "saves 'true'/'false' to localStorage under 'cc_dark_mode'. Custom CSS selectors prefixed with 'body.dark' override background colors, "
        "card surfaces, and typography tokens. On initial app boot, initDarkMode() checks localStorage and restores the user's preferred theme.",
        "CSS"
    )
    
    pdf.qa_item(
        13,
        "What is Glassmorphism and how is it implemented in CampusConnect?",
        "Glassmorphism creates a frosted-glass visual effect. In CampusConnect, it is applied to the sticky header and modal cards using: "
        "(1) Semi-transparent background: rgba(255, 255, 255, 0.75), (2) Hardware-accelerated background blur: backdrop-filter: blur(16px) saturate(180%), "
        "(3) Translucent borders: border-bottom: 1px solid rgba(255, 255, 255, 0.5), and (4) Soft diffused drop-shadows.",
        "UI Design"
    )
    
    pdf.qa_item(
        14,
        "How does the responsive design adapt to mobile viewports?",
        "Following mobile-first principles: on mobile devices (<640px), the horizontal navigation collapses into a slide-out drawer, "
        "the marketplace grid switches from 3 columns to 1 column, category cards adapt to a 2-column layout, and modal dialogs expand to "
        "occupy the viewport width with padding to prevent horizontal scrolling.",
        "Responsive Web"
    )
    
    pdf.qa_item(
        15,
        "Why use a multi-step Wizard for posting requests instead of a single form?",
        "Based on cognitive load theory and Miller's Law in UI/UX design, presenting 10+ form fields at once increases form abandonment. "
        "Breaking the process into 4 focused steps (Category -> Content -> Logistics -> Economics) allows per-step validation, prevents user fatigue, "
        "and provides visual progress feedback through step dots.",
        "UX Design"
    )
    
    pdf.qa_item(
        16,
        "How does the Toast notification system handle rapid triggers?",
        "showToast(type, message) dynamically sets theme styles (success, error, warning, info), adds the '.show' class to trigger CSS slide-in transitions, "
        "and sets a 3500ms setTimeout() timer. If a new toast is triggered before the timer expires, clearTimeout() resets the countdown to ensure the new "
        "message is displayed for the full duration.",
        "Frontend"
    )
    
    pdf.qa_item(
        17,
        "What is the advantage of using Utility-First CSS (Tailwind) over pure custom CSS?",
        "Utility-first CSS provides standardized design tokens (spacing, color palettes, responsive breakpoints) directly in the markup. "
        "This eliminates class-naming fatigue (BEM conventions), avoids bloated custom stylesheets with redundant properties, and ensures consistency "
        "across components.",
        "CSS"
    )

    # Page 8: Viva Questions - Part 4 & Production Roadmap
    pdf.add_page()
    pdf.sub_header("Category 4: Security, Testing, & Future Enhancements")
    
    pdf.qa_item(
        18,
        "How does CampusConnect handle authentication security, and what is needed for production?",
        "Currently, passwords are verified against credentials stored in localStorage. This demonstrates registration validation, "
        "minimum length checks, and session states for academic demonstration. For production deployment: passwords must never be stored "
        "on the client. They should be salted and hashed using bcrypt on a secure server, transmitting JWTs over HTTPS in HTTP-only, secure cookies.",
        "Web Security"
    )
    
    pdf.qa_item(
        19,
        "How do you protect the application from Cross-Site Scripting (XSS)?",
        "XSS occurs when malicious JavaScript is injected through user input. In CampusConnect, text values are captured through DOM .value "
        "properties. To secure production applications, all user-supplied text rendered into template strings should pass through a sanitization "
        "library (such as DOMPurify) or use textContent to prevent script execution.",
        "Security"
    )
    
    pdf.qa_item(
        20,
        "What testing strategies would you apply to verify this application?",
        "(1) Unit Testing: Testing utility functions (commission calculations, date formatting, filter logic) using Jest. "
        "(2) Integration Testing: Verifying that completing a task correctly updates provider stats, triggers notifications, and recalculates ratings. "
        "(3) End-to-End (E2E) Testing: Automating full user journeys (Register -> Post Request -> Switch User -> Accept -> Complete -> Rate) using Cypress or Playwright.",
        "Quality Assurance"
    )
    
    pdf.qa_item(
        21,
        "How would you integrate real payment gateways (e.g., UPI, Razorpay, Stripe)?",
        "When a user posts a paid task, the client triggers the Razorpay Checkout SDK. The payment is held in an escrow account. "
        "Upon task completion and mutual confirmation, a server-side webhook triggers an automated payout to the provider's registered "
        "UPI ID or bank account, deducting the 10% platform commission automatically.",
        "FinTech"
    )
    
    pdf.qa_item(
        22,
        "What is the future roadmap for CampusConnect?",
        "Future enhancements include: (1) University email verification (.edu / @college.ac.in) for campus authentication, "
        "(2) Real-time in-app messaging between requester and provider using WebSockets (Socket.io), (3) Geofenced campus beacon verification "
        "to confirm physical presence, and (4) Progressive Web App (PWA) support with service workers for offline caching.",
        "Roadmap"
    )
    
    pdf.output(output_path)
    print(f"Report generated successfully: {output_path}")

if __name__ == "__main__":
    out_dir = r"d:\Campus connect"
    out_file = os.path.join(out_dir, "CampusConnect_College_Report_and_Viva_QA.pdf")
    generate_full_report(out_file)
