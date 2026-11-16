# -*- coding: utf-8 -*-
"""Generate the SapporoSys static site."""
import html
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def e(value):
    return html.escape(str(value), quote=True)

def prefix(path):
    if "/" not in path:
        return "./"
    return "../" * path.count("/")

def asset(path, rel):
    return prefix(path) + rel

def logo_img(path):
    src = asset(path, "assets/images/brand/logo.jpg")
    return f'<img class="logo-img" src="{e(src)}" alt="SapporoSys Technologies">'

CHECK = '''<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><polyline points="20 6 9 17 4 12"></polyline></svg>'''

def _icon(inner):
    return (
        '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" '
        'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
        + inner + "</svg>"
    )

ICONS = {
    "layers": _icon('<path d="m12 3 9 5-9 5-9-5 9-5Z"/><path d="m3 12 9 5 9-5"/><path d="m3 16 9 5 9-5"/>'),
    "users": _icon('<path d="M16 21v-2a4 4 0 0 0-4-4H7a4 4 0 0 0-4 4v2"/><circle cx="9.5" cy="7" r="3"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a3 3 0 0 1 0 5.75"/>'),
    "calendar": _icon('<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>'),
    "stack": _icon('<rect x="3" y="4" width="18" height="6" rx="1"/><rect x="3" y="14" width="18" height="6" rx="1"/>'),
    "life": _icon('<path d="M19.5 12.6 12 20l-7.5-7.4a4.5 4.5 0 0 1 6.4-6.3L12 7.4l1.1-1.1a4.5 4.5 0 0 1 6.4 6.3Z"/>'),
    "key": _icon('<circle cx="8" cy="15" r="4"/><path d="m11.5 12.5 8-8M16 6l2 2M14 8l2 2"/>'),
    "code": _icon('<path d="m8 8-4 4 4 4M16 8l4 4-4 4M13 6l-2 12"/>'),
    "phone": _icon('<rect x="7" y="2" width="10" height="20" rx="2"/><path d="M11 18h2"/>'),
    "globe": _icon('<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18 14 14 0 0 1 0-18"/>'),
    "box": _icon('<path d="m21 8-9-5-9 5v8l9 5 9-5V8Z"/><path d="m3 8 9 5 9-5M12 13v8"/>'),
    "chart": _icon('<path d="M4 19V5M4 19h16M7 15l4-5 3 3 5-7"/>'),
    "pin": _icon('<path d="M12 21s7-6 7-11a7 7 0 1 0-14 0c0 5 7 11 7 11Z"/><circle cx="12" cy="10" r="2.2"/>'),
    "pen": _icon('<path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L8 18l-4 1 1-4 11.5-11.5Z"/>'),
    "cpu": _icon('<rect x="6" y="6" width="12" height="12" rx="1.5"/><path d="M9 2v4M15 2v4M9 18v4M15 18v4M2 9h4M2 15h4M18 9h4M18 15h4"/>'),
    "building": _icon('<path d="M4 21V5l8-2 8 2v16M9 21v-6h6v6M9 8h.01M15 8h.01M9 12h.01M15 12h.01"/>'),
    "shield": _icon('<path d="M12 3 5 6v6c0 4.5 3 7.5 7 9 4-1.5 7-4.5 7-9V6l-7-3Z"/><path d="m9 12 2 2 4-4"/>'),
    "route": _icon('<circle cx="6" cy="6" r="2"/><circle cx="18" cy="18" r="2"/><path d="M8 6h6a4 4 0 0 1 4 4v2M6 8v6a4 4 0 0 0 4 4h6"/>'),
    "search": _icon('<circle cx="11" cy="11" r="6"/><path d="m20 20-3.5-3.5"/>'),
    "clock": _icon('<circle cx="12" cy="12" r="8"/><path d="M12 8v5l3 2"/>'),
    "arrow": _icon('<path d="M5 12h14M13 6l6 6-6 6"/>'),
}

def icon(name):
    return f'<span class="ico">{ICONS[name]}</span>'

LINK_ARROW = '<svg class="link-arrow" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'

def card_block(title, text, icon_name, kicker="", more="", bullets=None, href=None, count=None):
    bits = [icon(icon_name)]
    if count is not None or kicker:
        num = ""
        if count is not None:
            shown = f"{int(count):02d}"
            num = f'<span class="count" data-count="{int(count)}" data-pad="2">{shown}</span>'
        sep = "  ·  " if num and kicker else ""
        bits.append(f'<p class="card-kicker">{num}{sep}{e(kicker)}</p>')
    bits.append(f"<h3>{e(title)}</h3><p>{e(text)}</p>")
    if more:
        bits.append(f'<p class="card-more">{e(more)}</p>')
    if bullets:
        bits.append('<ul class="card-points">' + "".join(f"<li>{e(b)}</li>" for b in bullets) + "</ul>")
    if href:
        bits.append(f'<span class="card-link">View {LINK_ARROW}</span>')
        return f'<a class="card" href="{e(href)}">{"".join(bits)}</a>'
    return f'<article class="card">{"".join(bits)}</article>'

BUILD = [
    ("Discovery notes", "The workflow, the data, and the limits are written down before anyone picks a stack.", "pen", ["Who uses it on a normal morning", "What must be true on day one"]),
    ("A release you can use", "Software exercised against real tasks, not a slide that only looks finished.", "box", ["Clickable builds during the work", "A result a staff member can finish"]),
    ("Plain handover", "Repository, runbook, and a walkthrough with the people who will own it.", "key", ["Accounts transferred to you", "A walkthrough, not a zip file"]),
    ("After go-live", "A named engineer for defects, small changes, and the first month in production.", "life", ["Same team as the build", "Small fixes inside the window"]),
]
PLATFORM = [
    ("Fit to the operation", "Screens and roles that match how the team already works.", "layers", ["Roles named after real jobs", "Steps in the order staff do them"]),
    ("Connected records", "One source for customers, stock, staff, or orders, with an audit trail.", "stack", ["One record, not three lists", "A history of who changed what"]),
    ("Access that makes sense", "Permissions by role, so the right people see the right work.", "shield", ["Access by job, not by favour", "A clear path when someone leaves"]),
    ("Room to grow", "A structure that can take more sites, more users, or a new product line.", "chart", ["Another site without a rewrite", "Room for a new line of work"]),
]
INDUSTRY = [
    ("Daily jobs first", "The tasks staff repeat every morning, designed before the edge cases.", "clock", ["The opening routine first", "Exceptions scheduled as a later release"]),
    ("Records you can trust", "Status, history, and documents kept where the work happens.", "shield", ["Status visible to the next shift", "Documents attached to the job"]),
    ("Training included", "A short handover so a new hire can use the system without a long manual.", "users", ["A live walkthrough", "Notes the next hire can read"]),
    ("Support on call", "Fixes and small improvements after the first week live.", "phone", ["A named person to call", "Small changes while the habit forms"]),
]
GROWTH = [
    ("A clear offer", "Pages and campaigns that say what you sell and who it is for.", "pen", ["One offer per page", "A path to a real enquiry"]),
    ("Measurement", "Search, ads, and content tied to enquiries, not vanity counts.", "chart", ["Enquiries, not just visits", "A number the sales team recognises"]),
    ("Technical base", "Speed, structure, and markup that the rest of the marketing can stand on.", "globe", ["Pages that load cleanly", "Structure a search engine can read"]),
    ("A monthly read", "What changed, what we will try next, and what we will stop.", "calendar", ["A written monthly note", "Work we will stop, not only start"]),
]
AI = [
    ("A narrow job", "One task the model is allowed to do, with a person still in the loop.", "cpu", ["One job, not a general assistant", "A person can still override it"]),
    ("Your content", "Answers grounded in your documents, products, and policies.", "layers", ["Answers from your material", "Sources a reviewer can check"]),
    ("A safe fallback", "When the system is unsure, it hands the conversation to a person.", "shield", ["A clear handoff", "The context travels with the question"]),
    ("A measured pilot", "A small release first, then a wider one if the numbers hold.", "chart", ["A pilot with a date", "A wider release only if it holds"]),
]

def svc(slug, title, kicker, img, lead, challenge, points, group):
    return {
        "path": slug + "/index.html",
        "nav": "services",
        "kind": "service",
        "group": group,
        "title": title,
        "kicker": kicker,
        "img": img,
        "lead": lead,
        "challenge": challenge,
        "points": points,
        "outcomes": [
            ("key", "Owned by you", "The code, the content, and the accounts sit with your company.", "Repositories, domains, and the tools your team logs into are transferred in the handover."),
            ("calendar", "Visible dates", "A plan you can put on a calendar, with the risks named.", "Each phase has a date, an owner, and the one risk most likely to move it."),
            ("phone", "Someone to call", "Support does not end on the day the system goes live.", "The first month has a named engineer who already knows the system."),
        ],
    }

SERVICES = [
    svc("software-development", "Software Development", "Custom engineering", "desk",
        "SapporoSys designs and builds software around a specific business, then stays close enough to support it.",
        "Generic tools bend the company around the product. We would rather shape the product around the work.", BUILD, "Build"),
    svc("website-development", "Website Development", "Sites that sell", "screens",
        "Marketing sites and content platforms that load quickly and stay easy for your team to update.",
        "A slow or brittle site quietly loses the enquiries the rest of the company is paying to earn.", BUILD, "Build"),
    svc("website-design", "Website Design", "Interface and structure", "notes",
        "Page structure, type, and layout for companies that want a site to feel as considered as the product.",
        "Decoration without a path through the page makes visitors work too hard to ask for a conversation.", BUILD, "Build"),
    svc("web-application-development", "Web Application Development", "Tools in the browser", "code",
        "Browser applications for teams that have outgrown spreadsheets and shared inboxes.",
        "When the real process lives in side chats and private files, nobody can see the status of the work.", BUILD, "Build"),
    svc("web-app-ui-ux-design", "Web App UI and UX", "Product design", "collab",
        "Flows, screens, and interface writing for software people use every day, not once in a demo.",
        "A clever layout that staff avoid is more expensive than a plain one they finish their work in.", BUILD, "Build"),
    svc("mobile-app-development", "Mobile App Development", "Android and iOS", "phone",
        "Mobile products for field teams and customers, built for unreliable networks and everyday use.",
        "An app that only works on the office wifi fails the moment it meets a real shift.", BUILD, "Build"),
    svc("mobile-app-design", "Mobile App Design", "Small-screen product design", "phone",
        "Mobile interface design that respects thumbs, glare, and the few seconds a person has between tasks.",
        "Desktop layouts squeezed onto a phone create taps in the wrong place and forms nobody finishes.", BUILD, "Build"),
    svc("api-development", "API Development", "Connections between systems", "server",
        "APIs that let your product, your partners, and your internal tools share the same facts.",
        "Copying data between systems by hand is where orders, invoices, and patient records go missing.", BUILD, "Build"),
    svc("software-product-development", "Software Product Development", "From first version to release", "laptop",
        "We take a product from a rough brief to a release a company can sell, support, and extend.",
        "A first version that tries to include everything usually ships nothing the customer can rely on.", BUILD, "Build"),
    svc("saas-development", "SaaS Development", "Multi-tenant products", "desk",
        "Subscription software with accounts, billing hooks, and a path from one customer to many.",
        "A single-customer build is not a SaaS product until tenancy, access, and upgrades are designed.", BUILD, "Build"),
    svc("wordpress-development", "WordPress Development", "Editorial sites", "notes",
        "WordPress builds for teams that want editors in control without giving up speed or structure.",
        "A theme full of plugins is cheap to start and expensive the week an editor cannot publish.", BUILD, "Build"),
    svc("website-maintenance", "Website Maintenance", "Care after launch", "server",
        "Updates, monitoring, and small improvements so a live site does not quietly fall behind.",
        "Most outages we inherit started as a postponed update, not as a dramatic failure.", BUILD, "Build"),
    svc("erp-development", "ERP Development", "Operations software", "workshop",
        "ERP systems for companies that have outgrown a patchwork of sheets, chat, and desktop tools.",
        "When finance, stock, and delivery each keep a private list, the business argues with itself.", PLATFORM, "Platforms"),
    svc("crm-development", "CRM Development", "Customer records", "meet",
        "CRM built around your actual sales motion, from first enquiry through renewal.",
        "A borrowed pipeline makes the team log work twice and trust the record once.", PLATFORM, "Platforms"),
    svc("hrms-development", "HRMS Development", "People operations", "team",
        "HR software for leave, roles, documents, and the questions staff ask every week.",
        "People data scattered across inboxes is hard to audit and harder to explain to an employee.", PLATFORM, "Platforms"),
    svc("billing-invoicing-software", "Billing and Invoicing Software", "Money in, clearly", "notes",
        "Invoicing tools that match how you price work, collect payment, and explain a bill.",
        "Invoices assembled by hand slip dates, tax, and the line items a client will dispute.", PLATFORM, "Platforms"),
    svc("inventory-management-software", "Inventory Management", "Stock you can count", "retail",
        "Inventory systems for teams that need to know what is in the building and what is promised.",
        "A stock number nobody believes creates both empty shelves and dusty overstock.", PLATFORM, "Platforms"),
    svc("ecommerce-development", "Ecommerce Development", "Stores that can take volume", "retail",
        "Online stores and catalogues built for real orders, returns, and the people who pack them.",
        "A pretty storefront that cannot talk to stock or shipping becomes a queue of apologies.", PLATFORM, "Platforms"),
    svc("enterprise-ecommerce", "Enterprise Ecommerce", "Complex catalogues", "city",
        "Commerce for companies with many buyers, price lists, approvals, and regions.",
        "A consumer checkout does not survive contract pricing and a purchasing department.", PLATFORM, "Platforms"),
    svc("b2b-portal-development", "B2B Portal Development", "Partner and buyer portals", "collab",
        "Portals where distributors, buyers, or franchisees place orders and see their own account.",
        "Emailing spreadsheets to partners does not scale past the first busy season.", PLATFORM, "Platforms"),
    svc("business-process-automation", "Business Process Automation", "Less repeated work", "workshop",
        "Automation for the steps a team repeats: approvals, notices, handoffs, and status updates.",
        "Automation aimed at the wrong step just moves the delay somewhere harder to see.", PLATFORM, "Platforms"),
    svc("legacy-modernization", "Legacy Modernization", "Replace with care", "server",
        "We replace aging systems in slices, so the business keeps running while the new one takes over.",
        "A big-bang rewrite is how companies lose the only person who understood the old system.", PLATFORM, "Platforms"),
    svc("hospital-management-software", "Hospital Management Software", "Care operations", "clinic",
        "Software for appointments, wards, billing, and the handoff between departments.",
        "A hospital cannot pause while a system is redesigned. The daily board still has to be right.", INDUSTRY, "Industry"),
    svc("hotel-management-software", "Hotel Management Software", "Rooms and guests", "city",
        "Front desk, housekeeping, and billing tools for properties that juggle rooms and walk-ins.",
        "When the desk and housekeeping keep different lists, a guest arrives to a room that is not ready.", INDUSTRY, "Industry"),
    svc("school-management-software", "School Management Software", "Campus operations", "notes",
        "Systems for admissions, attendance, fees, and the messages a school sends home.",
        "Parents and teachers lose trust quickly when the same child has two different records.", INDUSTRY, "Industry"),
    svc("coaching-institute-software", "Coaching Institute Software", "Batches and fees", "laptop",
        "Software for batches, tests, fees, and the follow-up a coaching centre does every evening.",
        "A centre run from chat groups cannot see who has paid, who has attended, or who is slipping.", INDUSTRY, "Industry"),
    svc("logistics-software", "Logistics Software", "Movement of goods", "city",
        "Dispatch, tracking, and proof of delivery for operators who live by the day's routes.",
        "A late status update is not a small bug when a truck is already at the wrong dock.", INDUSTRY, "Industry"),
    svc("real-estate-portal-development", "Real Estate Portals", "Listings and leads", "city",
        "Property portals and broker tools for listings, enquiries, and site visits.",
        "Leads that sit in a personal inbox never become a pipeline the firm can manage.", INDUSTRY, "Industry"),
    svc("travel-portal-development", "Travel Portal Development", "Trips and inventory", "office",
        "Travel portals for search, booking, and the changes that happen after a ticket is issued.",
        "Travel inventory moves fast. A portal that lags the supplier creates bookings you cannot honour.", INDUSTRY, "Industry"),
    svc("ai-development", "AI Development", "Practical automation", "code",
        "Applied AI for a specific job: sorting requests, drafting replies, or reading your own documents.",
        "A model with no boundary will sound confident about things your company never said.", AI, "Intelligence"),
    svc("ai-chatbot-development", "AI Chatbots", "Conversations with a limit", "screens",
        "Chatbots that answer from your knowledge and pass the rest to a person with the context attached.",
        "A bot that traps a customer is worse than a contact form. The handoff has to be obvious.", AI, "Intelligence"),
    svc("ai-voice-agents", "AI Voice Agents", "Phone workflows", "phone",
        "Voice agents for bookings, status checks, and after-hours calls, with a clean transfer to staff.",
        "A voice system that cannot admit uncertainty will book the wrong thing in a confident tone.", AI, "Intelligence"),
    svc("seo-services", "SEO Services", "Search that matches the offer", "notes",
        "Technical and on-page SEO for companies that want the right enquiries, not just more traffic.",
        "Rankings without a page that can take the enquiry are a report, not a result.", GROWTH, "Growth"),
    svc("international-seo", "International SEO", "More than one market", "city",
        "Search structure for companies selling in more than one language or country.",
        "One page trying to rank everywhere usually ranks clearly nowhere.", GROWTH, "Growth"),
    svc("digital-marketing", "Digital Marketing", "Demand with a system", "collab",
        "Campaigns, content, and landing pages planned against the enquiries your team can actually take.",
        "Traffic that the sales team cannot follow up is a cost, even when the dashboard looks busy.", GROWTH, "Growth"),
    svc("ppc-management", "PPC Management", "Paid media", "desk",
        "Paid search and paid social run against a landing page and an offer, then read every month.",
        "Spend without a sentence that says who should click is how budgets disappear.", GROWTH, "Growth"),
    svc("social-media-marketing", "Social Media Marketing", "A public voice", "team",
        "Social programmes with a point of view, a cadence, and a path back to a conversation.",
        "Posting because the calendar is empty teaches an audience nothing about the work.", GROWTH, "Growth"),
    svc("software-development-company-usa", "Software Development Company in the USA", "United States", "city",
        "SapporoSys works with US teams on custom software, with overlapping hours and a written handover.",
        "Distance only hurts when decisions are verbal and the record lives in one time zone.", BUILD, "Places"),
    svc("software-development-company-uk", "Software Development Company in the UK", "United Kingdom", "office",
        "A UK-facing practice for product builds, portals, and the support that follows a release.",
        "UK buyers usually need a clear data story and a supplier who will still answer after launch.", BUILD, "Places"),
    svc("software-development-company-uae", "Software Development Company in the UAE", "United Arab Emirates", "city",
        "Software for UAE operators: portals, commerce, and internal tools built around local ways of working.",
        "A product copied from another market misses the approvals, languages, and hours that matter on the ground.", BUILD, "Places"),
    svc("software-development-company-canada", "Software Development Company in Canada", "Canada", "meet",
        "Canadian engagements for teams that want a build partner rather than a rotating bench.",
        "The useful overlap is not just the clock. It is a single plan both sides can read.", BUILD, "Places"),
    svc("software-development-company-australia", "Software Development Company in Australia", "Australia", "workshop",
        "Australia-facing delivery for products that have to keep working while our two days barely meet.",
        "Async only works when the day's decisions are written down before one side goes home.", BUILD, "Places"),
]

COMPANY = {
    "about-us": ("About SapporoSys", "The studio", "team",
                 "SapporoSys is a software studio. We design, build, and look after systems for companies that want the work explained in plain language.",
                 "The practice started with a simple complaint: too many projects were handed over as a folder of code and a farewell. We stay through the first real month of use."),
    "our-process": ("How We Work", "Four stages", "workshop",
                    "Every engagement moves through discovery, a written plan, a build you can see, and a launch that includes support.",
                    "We do not start from a stack. We start from the job the software has to take off someone's desk."),
    "our-team": ("Our Team", "Who does the work", "collab",
                 "Producers, designers, and engineers who stay on the same engagement from the first workshop to the support window.",
                 "You will meet the people who write the system. The sales conversation is not a different company from the build."),
    "why-choose-us": ("Why SapporoSys", "How we choose the work", "desk",
                      "We take fewer projects so a senior person can still name the risks on yours.",
                      "The useful promise is not speed at any cost. It is a date, a scope, and a system your team can keep."),
    "partners-certifications": ("Partners and Practice", "How we work with others", "meet",
                                "We partner with specialist firms when a project needs a skill we should not pretend to have in-house.",
                                "Certifications matter less to us than a recent release you can click through. We will still show the tools we use and why."),
    "technology-stack": ("Technology Stack", "Tools we actually ship", "server",
                         "The stack follows the problem: usually a typed web app, a managed database, and a host we can explain to your team.",
                         "We pick boring, well-supported tools on purpose. Fashion is a poor reason to take on a dependency."),
    "testimonials": ("Client Notes", "After the release", "office",
                     "A few words from teams who have taken a product from brief to a system their staff use.",
                     "We ask for notes after the support window, not on the day of the demo."),
    "life-at-company": ("A Week at the Studio", "How the days go", "workshop",
                        "Mornings are for reviews and writing things down. Afternoons are for building. Fridays close with what shipped and what slipped.",
                        "The studio is quiet on purpose. The work is easier to see when the day has a shape."),
    "life-at-company-name": ("The SapporoSys Name", "Why the mark looks like this", "notes",
                             "The mark is a folded S. Sapporo is set in white and Sys in blue, with Technologies underneath, because the work is systems people have to run.",
                             "The name is the practice, not a slogan. The same mark sits on estimates, release notes, and the project folder."),
    "life-at-luminate": ("Studio Life", "The room the work is made in", "team",
                         "This page is the studio diary: how we hire, how we review, and how a new person learns a client system.",
                         "Same standard on an internal tool and on a product a customer will pay for."),
    "industries": ("Industries", "Where the work lands", "city",
                   "Healthcare, logistics, education, hospitality, retail, property, and software companies themselves.",
                   "We do not pretend every industry is the same. We do insist the first workshop is about their day, not our menu."),
}

LOCATIONS = [
    ("locations/usa", "United States", "New York and remote US hours", "city"),
    ("locations/uk", "United Kingdom", "London overlap, written decisions", "office"),
    ("locations/uae", "United Arab Emirates", "Dubai-facing delivery", "city"),
    ("locations/canada", "Canada", "Toronto overlap", "meet"),
    ("locations/australia", "Australia", "Async by design", "workshop"),
]

FAQS = [
    ("Who owns the code?", "You do. Repositories, designs, and content accounts are transferred as part of handover, not held as leverage."),
    ("Do you only work with large companies?", "No. The useful client is one with a real operation and someone who can make a decision. Size is secondary."),
    ("Can you join a team we already have?", "Yes. We can take a slice of a product, with your engineers in the reviews, or take the build and hand it back."),
    ("How do projects start?", "A call, then a short written brief. If the shape is still unclear we propose a paid discovery instead of guessing a fixed price."),
    ("What does support include?", "Defects, small changes, and a person who already knows the system. Larger new work is scoped separately so the care window stays honest."),
    ("Where are you based?", "The studio is in Bengaluru. Project hours overlap the US, UK, UAE, Canada, and Australia as the engagement needs."),
]

ROLES = [
    ("Product engineer", "Bengaluru or remote", "Web applications, APIs, and the unglamorous edges of a release."),
    ("Mobile engineer", "Bengaluru", "Android and iOS products with offline moments and careful releases."),
    ("Delivery producer", "Bengaluru", "Plans, risks, and the written record clients actually read."),
    ("Product designer", "Remote in India", "Flows and interface writing for software people use on a Tuesday."),
]

LEGAL = {
    "privacy-policy": ("Privacy Policy", [
        "SapporoSys collects the details you type into a form: name, work email, company, and the description of a project. We use them to reply to that enquiry.",
        "We do not sell enquiry data. We do not run third-party advertising pixels on this site.",
        "Messages are stored in the mailbox that receives them and kept only as long as the conversation, or a later project, needs them.",
        "To ask for a copy or a deletion, write to hello@sapporosys.com. If we are mid-project, some records have to stay for the contract.",
    ]),
    "terms-conditions": ("Terms and Conditions", [
        "This website describes services. It is not itself an offer to start work. Work begins when both sides accept a written scope.",
        "Estimates are estimates until a scope, a date, and a fee are signed. Discovery, if needed, is its own small engagement.",
        "You are responsible for the accuracy of the materials you send us. We are responsible for the work described in the scope.",
        "Either side can end a negotiation before signature without fee. After signature, the contract governs, not this page.",
    ]),
    "refund-policy": ("Refund Policy", [
        "Discovery fees and paid workshops are for time already spent. They are not refunded once the session has happened.",
        "If a fixed-scope build stops before an agreed milestone, we bill the milestone in progress and return any amount paid ahead of work not started.",
        "Retainers for support are billed monthly. A month already begun is not refunded. You can stop the next month with the notice in the agreement.",
        "Questions about a charge go to hello@sapporosys.com with the invoice number.",
    ]),
}

BLOG = [
    ("pen", "What a first release should leave out", "Scope", "The features that make a first version feel complete are often the ones that keep it from shipping.", "A first release is the smallest system that lets a real user finish a real job. The left-out list is part of the plan.", "6 min read"),
    ("key", "Handover is a product", "Delivery", "A repository without a walkthrough is a locked drawer. We treat the handover as part of the build.", "Accounts, a runbook, and an hour with the people who will own the system. The zip file is the least of it.", "5 min read"),
    ("life", "Support is not a leftover", "Care", "The week after launch is when staff find the real edge cases. Plan for that week on purpose.", "The support window is scheduled with the same team, so the first real month is not an afterthought.", "4 min read"),
]


def logo_link(path):
    return f'<a class="logo" href="{e(prefix(path) + "index.html")}" aria-label="SapporoSys home">{logo_img(path)}</a>'

def drop(label, columns, end=False, on=False, extra=""):
    klass = "drop" + (" drop-end" if end else "") + (" is-on" if on else "")
    cols = []
    for kicker, links in columns:
        items = "".join(
            f'<a href="{e(href)}"><strong>{e(text)}</strong><span>{e(desc)}</span></a>'
            for text, desc, href in links
        )
        cols.append(f'<div class="drop-col"><p class="drop-kicker">{e(kicker)}</p>{items}</div>')
    return f'<div class="{klass}"><button type="button" aria-expanded="false">{e(label)} <svg class="caret" viewBox="0 0 12 12" aria-hidden="true"><path d="M2.5 4.5 6 8l3.5-3.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg></button><div class="drop-panel">{"".join(cols)}{extra}</div></div>'

def nav(path, active):
    p = prefix(path)
    services = [
        ("Build", [
            ("Software", "Custom systems for a real operation.", p + "software-development/index.html"),
            ("Websites", "Sites your team can keep updating.", p + "website-development/index.html"),
            ("Mobile apps", "Android and iOS for daily use.", p + "mobile-app-development/index.html"),
            ("Product and SaaS", "From a first version to a release.", p + "saas-development/index.html"),
        ]),
        ("Grow", [
            ("AI", "Narrow automation with a person in the loop.", p + "ai-development/index.html"),
            ("ERP and CRM", "Operations software past the spreadsheet.", p + "erp-development/index.html"),
            ("Ecommerce", "Stores that can take a real order.", p + "ecommerce-development/index.html"),
            ("SEO and marketing", "Search and campaigns tied to enquiries.", p + "seo-services/index.html"),
        ]),
    ]
    company = [
        ("Company", [
            ("About", "Who the studio is.", p + "about-us/index.html"),
            ("How we work", "Discovery through support.", p + "our-process/index.html"),
            ("Team", "The people on the work.", p + "our-team/index.html"),
            ("Careers", "Open roles.", p + "careers/index.html"),
        ]),
        ("More", [
            ("Why SapporoSys", "How we choose tools and dates.", p + "why-choose-us/index.html"),
            ("FAQs", "Before a project starts.", p + "faqs/index.html"),
            ("Locations", "Where the hours overlap.", p + "locations/index.html"),
            ("Industries", "The operations we know.", p + "industries/index.html"),
        ]),
    ]
    work = [
        ("Work", [
            ("Notes", "Writing from the studio.", p + "blog/index.html"),
            ("Client notes", "Words from teams we have built with.", p + "testimonials/index.html"),
        ]),
    ]
    home = f'<a href="{e(p + "index.html")}" class="{"is-on" if active == "home" else ""}">Home</a>'
    portfolio = f'<a href="{e(p + "portfolio/index.html")}" class="{"is-on" if active == "portfolio" else ""}">Portfolio</a>'
    cases = f'<a href="{e(p + "case-studies/index.html")}" class="{"is-on" if active == "cases" else ""}">Case studies</a>'
    contact = f'<a href="{e(p + "contact-us/index.html")}" class="{"is-on" if active == "contact" else ""}">Contact</a>'
    all_services = f'<a class="drop-all" href="{e(p + "services/index.html")}">All services</a>'
    return home + drop("Services", services, on=active == "services", extra=all_services) + drop("Company", company, on=active == "company") + drop("Work", work, end=True, on=active == "work") + portfolio + cases + contact

def header(path, active):
    p = prefix(path)
    return f'''<div class="utility"><div class="wrap utility-row"><span class="utility-note">Software studio · Bengaluru, working across time zones</span><span class="utility-links"><a href="tel:+918041207788">+91 80 4120 7788</a><a href="mailto:hello@sapporosys.com">hello@sapporosys.com</a></span></div></div>
<header class="site-header"><div class="wrap bar">{logo_link(path)}
<nav class="nav" aria-label="Primary">{nav(path, active)}</nav>
<a class="btn btn-saffron header-cta" href="{e(p + "request-a-quote/index.html")}">Start a brief</a>
<button class="burger" type="button" aria-label="Open menu" aria-expanded="false"><i></i><i></i><i></i></button>
</div></header>'''

def footer(path):
    p = prefix(path)
    cols = [
        ("Practice", [("Software", "software-development/"), ("Mobile", "mobile-app-development/"), ("Web", "website-development/"), ("All services", "services/")]),
        ("Company", [("About", "about-us/"), ("How we work", "our-process/"), ("Careers", "careers/"), ("Locations", "locations/")]),
        ("Visit", [("Portfolio", "portfolio/"), ("Case studies", "case-studies/"), ("FAQs", "faqs/"), ("Contact", "contact-us/")]),
    ]
    blocks = []
    for title, links in cols:
        items = "".join(f'<li><a href="{e(p + href + "index.html")}">{e(text)}</a></li>' for text, href in links)
        blocks.append(f'<div><h2>{e(title)}</h2><ul>{items}</ul></div>')
    return f'''<footer class="site-footer"><div class="wrap"><div class="foot-grid"><div class="foot-brand">{logo_img(path)}<p>Custom software, mobile products, and the support that follows a release. SapporoSys, Bengaluru.</p><p><a href="tel:+918041207788">+91 80 4120 7788</a><br><a href="mailto:hello@sapporosys.com">hello@sapporosys.com</a></p></div>{"".join(blocks)}</div>
<div class="foot-bottom"><div>© 2026 SapporoSys. All rights reserved.</div><div class="legal-links"><a href="{e(p + "refund-policy/index.html")}">Refunds</a><a href="{e(p + "privacy-policy/index.html")}">Privacy</a><a href="{e(p + "terms-conditions/index.html")}">Terms</a><a href="{e(p + "sitemap.html")}">Sitemap</a></div></div>
<p class="media-note">Photographs and video are from Pexels and are free to use, including for commercial projects.</p></div></footer>'''

def shell(path, title, desc, active, body):
    p = prefix(path)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="icon" href="{e(asset(path, "assets/images/brand/favicon.png"))}" type="image/png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@500;600&family=Manrope:wght@400;500;600;700&family=Syne:wght@600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{e(asset(path, "assets/css/site.css"))}?v=3">
</head>
<body class="has-film">
<a class="skip" href="#main">Skip to content</a>
{header(path, active)}
<main id="main">{body}</main>
{footer(path)}
<script src="{e(asset(path, "assets/js/site.js"))}?v=4"></script>
</body>
</html>
'''

def crumbs(path, items):
    p = prefix(path)
    bits = [f'<a href="{e(p + "index.html")}">Home</a>']
    for text, href in items[:-1]:
        bits.append(f'<a href="{e(p + href)}">{e(text)}</a>')
    bits.append(f'<span>{e(items[-1][0])}</span>')
    return '<p class="crumbs">' + " / ".join(bits) + "</p>"

def cta(path):
    p = prefix(path)
    return f'''<section class="cta"><div class="wrap"><p class="kicker">Start a brief</p><h2>Tell us the job the software should take on.</h2><p>A call or a note is enough. If the shape is unclear, we will suggest a short discovery instead of a guess.</p><div class="actions"><a class="btn btn-saffron" href="{e(p + "request-a-quote/index.html")}">Request an estimate</a><a class="btn btn-ghost" href="{e(p + "contact-us/index.html")}">Contact the studio</a></div></div></section>'''

def img(path, name, alt):
    return f'<img src="{e(asset(path, "assets/media/" + name + ".jpg"))}" alt="{e(alt)}">'

def form_block(intro):
    return f'''<form class="form" data-form>
<p class="form-ok">{e(intro)}</p>
<div class="fields">
<label>Full name <span class="req">*</span><input name="name" required autocomplete="name"></label>
<label>Work email <span class="req">*</span><input name="email" type="email" required autocomplete="email"></label>
</div>
<div class="fields">
<label>Company<input name="company" autocomplete="organization"></label>
<label>What do you need? <span class="req">*</span>
<select name="need" required>
<option value="">Choose one</option>
<option>Custom software</option>
<option>Web or mobile product</option>
<option>Operations system</option>
<option>AI assistant</option>
<option>Marketing site and SEO</option>
<option>Something else</option>
</select></label>
</div>
<label>Project notes <span class="req">*</span><textarea name="notes" required placeholder="The operation, the deadline you care about, and what has already been tried."></textarea></label>
<button class="btn btn-saffron btn-wide" type="submit">Send the brief</button>
</form>'''

def film(path, kicker, title_html, lead, extra="", image="desk", video=None, crumbs_html=""):
    poster = asset(path, f"assets/media/{image}.jpg")
    if video:
        src = asset(path, f"assets/media/{video}.mp4")
        media = f'<video class="hero-still" autoplay muted loop playsinline poster="{e(poster)}"><source src="{e(src)}" type="video/mp4"></video>'
    else:
        media = f'<img class="hero-still" src="{e(poster)}" alt="">'
    return (
        f'<section class="hero-film">{media}<div class="scrim"></div>'
        f'<div class="wrap hero-copy">{crumbs_html}<p class="kicker">{e(kicker)}</p>'
        f'<h1 class="display">{title_html}</h1><p class="lede">{e(lead)}</p>{extra}</div></section>'
    )

def home():
    path = "index.html"
    p = prefix(path)
    rows = ""
    featured = [
        ("software-development", "code"),
        ("mobile-app-development", "phone"),
        ("website-development", "globe"),
        ("ai-development", "cpu"),
        ("erp-development", "layers"),
        ("saas-development", "stack"),
    ]
    for i, (slug, ic) in enumerate(featured, 1):
        item = next(s for s in SERVICES if s["path"].startswith(slug + "/"))
        rows += card_block(item["title"], item["lead"], ic, kicker=item["kicker"], count=i, more=item["challenge"], href=p + item["path"])
    checks = "".join(f"<li>{CHECK}{e(t)}</li>" for t in ["Custom software and internal tools", "Web and mobile products", "A written plan before the build", "Support after the release"])
    steps = "".join(
        f'<div class="step"><b class="count" data-count="{n}" data-pad="2">{n:02d}</b><div><h3>{e(h)}</h3><p>{e(t)}</p></div></div>'
        for n, h, t in [
            (1, "Discover", "We learn the job, the people, and the constraints before a stack is chosen."),
            (2, "Plan", "A sequence, a date, and the result you will be able to point at."),
            (3, "Build", "Reviewed work you can click through while it is still in progress."),
            (4, "Launch", "Release, training, and a support window with the same team."),
        ]
    )
    reasons = "".join(
        card_block(h, t, ic, count=n, more=more, bullets=bullets)
        for n, ic, h, t, more, bullets in [
            (1, "layers", "Built for one operation", "The software follows the work you already do.",
             "We write the morning routine before a stack is chosen, so the system matches the desk it lands on.",
             ["Screens named in your words", "Roles for the people who do the job"]),
            (2, "users", "Senior people on the job", "The team you meet is the team that ships.",
             "Reviews include the engineers and designers doing the work, not a separate bench introduced after the sale.",
             ["The same names from workshop to release", "No silent handoff to a new team"]),
            (3, "calendar", "Dates in writing", "Scope and risk stay visible, not implied.",
             "A date without the risk next to it is a wish. We put both on the plan you can share.",
             ["A date for each phase", "The risk that could move it"]),
            (4, "stack", "Tools that will still be here", "We prefer supported platforms over fashion.",
             "The stack is something your team can hire for in two years, not a framework we have to explain forever.",
             ["Supported platforms", "A choice we can defend in writing"]),
            (5, "life", "Care after launch", "The first real month is part of the engagement.",
             "Staff find the real edge cases in the week after go-live. That week is scheduled, not hoped for.",
             ["A named engineer after release", "Small fixes inside the window"]),
            (6, "key", "Yours to keep", "Code, content, and accounts transfer to you.",
             "The repository, the content, and the logins are part of the handover, not a later negotiation.",
             ["You hold the accounts", "A walkthrough with your team"]),
        ]
    )
    actions = (
        f'<div class="actions"><a class="btn btn-saffron" href="{e(p + "request-a-quote/index.html")}">Start a brief</a>'
        f'<a class="btn btn-ink" href="{e(p + "services/index.html")}">See the practice</a></div>'
        f'<p class="fine"><a href="tel:+918041207788">+91 80 4120 7788</a> · <a href="mailto:hello@sapporosys.com">hello@sapporosys.com</a></p>'
    )
    opening = film(path, "SapporoSys", "Software with a <em>clear</em> owner.",
                   "We design custom systems, web and mobile products, and the support that keeps them useful after launch.",
                   actions, "code", "code")
    body = f'''
{opening}
<section class="stat-strip"><div class="wrap stats">
<div class="stat"><b class="count" data-count="140">140</b><span>Products still in use</span></div>
<div class="stat"><b class="count" data-count="11">11</b><span>Years of the practice</span></div>
<div class="stat"><b class="count" data-count="64">64</b><span>Engineers and designers</span></div>
<div class="stat"><b class="count" data-count="4">4</b><span>Hour-bands we cover</span></div>
</div></section>
<div class="marquee" aria-hidden="true"><div class="marquee-track"><span>Healthcare</span><i>·</i><span>Logistics</span><i>·</i><span>Education</span><i>·</i><span>Hospitality</span><i>·</i><span>Retail</span><i>·</i><span>Property</span><i>·</i><span>Finance</span><i>·</i><span>Startups</span><i>·</i><span>Healthcare</span><i>·</i><span>Logistics</span><i>·</i><span>Education</span><i>·</i><span>Hospitality</span><i>·</i><span>Retail</span><i>·</i><span>Property</span><i>·</i><span>Finance</span><i>·</i><span>Startups</span><i>·</i></div></div>
<section class="section"><div class="wrap split">
<figure class="photo-frame">{img(path, "team", "Engineers reviewing work together")}<figcaption class="caption">Reviews happen in the room, not only in a ticket.</figcaption></figure>
<div>
<p class="kicker">The studio</p>
<h2>A build partner that does not disappear at launch.</h2>
<p class="lede">SapporoSys is independent. We take a brief, write the plan, ship the system, and stay for the first weeks of real use.</p>
<ul class="checks">{checks}</ul>
<a class="link-more" href="{e(p + "about-us/index.html")}">About the studio</a>
</div>
</div></section>
<section class="section" style="padding-top:0"><div class="wrap">
<div class="section-head"><div><p class="kicker">Practice</p><h2>Where most briefs begin.</h2></div><p>Six starting points, with the problem each one is meant to take off a desk. The full list is grouped the way we staff the work.</p></div>
<div class="cards cards-3">{rows}</div>
</div></section>
<section class="section" style="padding-top:0"><div class="wrap steps">
<figure class="photo-frame"><video autoplay muted loop playsinline poster="{e(asset(path, "assets/media/meet.jpg"))}"><source src="{e(asset(path, "assets/media/studio.mp4"))}" type="video/mp4"></video></figure>
<div>
<p class="kicker">Method</p>
<h2>A short path from brief to launch.</h2>
<div class="step-list">{steps}</div>
</div>
</div></section>
<section class="section" style="padding-top:0"><div class="wrap">
<div class="section-head"><div><p class="kicker">Why this studio</p><h2>Work you can put on a calendar.</h2></div><p>The same rules on a first marketing site and on a product that already has customers.</p></div>
<div class="cards cards-3">{reasons}</div>
</div></section>
<section class="section" style="padding-top:0"><div class="wrap">
<div class="section-head"><div><p class="kicker">Clients</p><h2>Notes from after the release.</h2></div><p>Asked once the support window had started, not on demo day.</p></div>
<div class="quotes">
<figure class="quote"><blockquote>“They wrote the plan in language our operators understood, then built the thing the plan described.”</blockquote><figcaption>Meera Iyer · Operations lead, Northwind Clinics</figcaption></figure>
<div class="quote-side">
<figure class="quote-sm"><blockquote>“The handover included the people, not only the repository.”</blockquote><figcaption>Jonas Adler · Product, Fieldnote</figcaption></figure>
<figure class="quote-sm"><blockquote>“Dates slipped once, and we heard about it before we had to ask.”</blockquote><figcaption>Leila Hassan · Director, Harbour Goods</figcaption></figure>
</div>
</div>
</div></section>
{cta(path)}'''
    return shell(path, "SapporoSys — Custom software, apps, and support", "SapporoSys designs custom software, web and mobile products, and supports them after launch.", "home", body)

def service_page(item):
    path = item["path"]
    p = prefix(path)
    cards = "".join(card_block(h, t, ic, bullets=bullets) for h, t, ic, bullets in item["points"])
    outcomes = "".join(card_block(h, t, ic, more=extra) for ic, h, t, extra in item["outcomes"])
    actions = f'<div class="actions"><a class="btn btn-saffron" href="{e(p + "request-a-quote/index.html")}">Request an estimate</a><a class="btn btn-ink" href="{e(p + "contact-us/index.html")}">Talk to the studio</a></div>'
    clip = "build" if item["path"].startswith("software-development/") else None
    opening = film(path, item["kicker"], e(item["title"]), item["lead"], actions, item["img"], clip, crumbs(path, [("Services", "services/index.html"), (item["title"], "")]))
    body = f'''
{opening}
<section class="band"><div class="wrap split"><div><p class="kicker">The problem</p><h2>Why this work usually stalls.</h2></div><p>{e(item["challenge"])}</p></div></section>
<section class="section"><div class="wrap"><div class="section-head"><div><p class="kicker">What you receive</p><h2>Concrete, not a menu.</h2></div><p>Each engagement names the deliverables before the build starts.</p></div><div class="cards">{cards}</div></div></section>
<section class="section" style="padding-top:0"><div class="wrap"><div class="section-head"><div><p class="kicker">After the release</p><h2>What stays true on every engagement.</h2></div><p>These three hold whether the work is a first marketing site or a system that already has users.</p></div><div class="cards cards-3">{outcomes}</div></div></section>
{cta(path)}'''
    return shell(path, item["title"] + " | SapporoSys", item["lead"], "services", body)

def services_index():
    path = "services/index.html"
    groups = []
    for name in ["Build", "Platforms", "Industry", "Intelligence", "Growth", "Places"]:
        items = [s for s in SERVICES if s["group"] == name]
        group_icon = {"Build": "code", "Platforms": "layers", "Industry": "building", "Intelligence": "cpu", "Growth": "chart", "Places": "pin"}[name]
        cards = "".join(
            card_block(s["title"], s["lead"], group_icon, kicker=s["kicker"], more=s["challenge"], href=prefix(path) + s["path"])
            for s in items
        )
        groups.append(f'<div class="group"><h2>{e(name)}</h2><div class="mini-grid">{cards}</div></div>')
    opening = film(path, "Practice", "Everything the studio takes on.", "Grouped the way we staff the work: build, platforms, industry systems, intelligence, growth, and the places we overlap hours with.", "", "screens", "studio", f'<p class="crumbs"><a href="{e(prefix(path) + "index.html")}">Home</a> / <span>Services</span></p>')
    body = f'''{opening}
<section class="section" style="padding-top:0"><div class="wrap">{"".join(groups)}</div></section>{cta(path)}'''
    return shell(path, "Services | SapporoSys", "Software, platforms, industry systems, AI, and growth services from SapporoSys.", "services", body)

def story_page(slug, title, kicker, image, lead, more, active="company"):
    path = slug + "/index.html"
    points = [
        ("pen", "A written plan", "Scope, date, and the result, before the build is priced as a guess.",
         "The plan is short enough to share with the person who will use the system.", ["What is in the first release", "What is deliberately left out"]),
        ("users", "The same people", "Reviews include the engineers and designers doing the work.",
         "You will not meet one team to sell the work and another team to build it.", ["Names you can write to", "Reviews on the working build"]),
        ("life", "A support window", "Launch includes the first weeks of real use, not a farewell email.",
         "The week staff start relying on the system is part of the schedule.", ["A named engineer", "Small fixes while habits form"]),
    ]
    cards = "".join(card_block(h, t, ic, more=more, bullets=bullets) for ic, h, t, more, bullets in points)
    clip = "studio" if slug == "about-us" else None
    opening = film(path, kicker, e(title), lead, "", image, clip, crumbs(path, [(title, "")]))
    body = f'''{opening}
<section class="band"><div class="wrap wrap-s"><p>{e(more)}</p></div></section>
<section class="section"><div class="wrap cards cards-3">{cards}</div></section>{cta(path)}'''
    return shell(path, title + " | SapporoSys", lead, active, body)

def locations_index():
    path = "locations/index.html"
    p = prefix(path)
    place_copy = {
        "United States": ("pin", "New York hours with a written record the same day.", ["Reviews before the US evening", "Handover a local team can run"]),
        "United Kingdom": ("pin", "London overlap, with decisions written before either side signs off.", ["A data story you can share", "Support that continues after launch"]),
        "United Arab Emirates": ("pin", "Dubai-facing delivery around local approvals, languages, and hours.", ["Portals and internal tools", "A plan both offices can read"]),
        "Canada": ("pin", "Toronto overlap for teams that want one partner, not a rotating bench.", ["One plan, two time zones", "The same people on the reviews"]),
        "Australia": ("clock", "The days barely meet, so the work is written before one side goes home.", ["Decisions captured the same day", "A build that keeps moving overnight"]),
    }
    cards = "".join(
        card_block(name, blurb, place_copy[name][0], kicker="Working hours", more=place_copy[name][1], bullets=place_copy[name][2], href=p + slug + "/index.html")
        for slug, name, blurb, _img in LOCATIONS
    )
    opening = film(path, "Hours", "Where the working day overlaps.", "The studio is in Bengaluru. Engagements are staffed so decisions are not stuck overnight.", "", "city", None, crumbs(path, [("Locations", "")]))
    body = f'''{opening}
<section class="section" style="padding-top:0"><div class="wrap loc-grid">{cards}</div></section>{cta(path)}'''
    return shell(path, "Locations | SapporoSys", "SapporoSys works from Bengaluru with overlap for the US, UK, UAE, Canada, and Australia.", "company", body)

def location_page(slug, name, blurb, image):
    path = slug + "/index.html"
    lead = f"SapporoSys staffs {name} engagements so reviews land inside {blurb.lower()}."
    return story_page(slug, name, "Location", image, lead, blurb + ". Discovery notes are written the same day, so neither side waits on a memory.", "company")

def portfolio():
    path = "portfolio/index.html"
    projects = [
        ("clinic", "life", "Healthcare", "Northwind wards", "A ward board and billing handoff for a clinic group.", "Charge status and the ward list stopped living in two systems.", ["Discharge status visible to billing", "Fewer missed charges in the first quarter"]),
        ("retail", "box", "Retail", "Harbour Goods", "Stock and store orders for a regional retailer.", "The shop and the warehouse finally share one number.", ["Store orders without retyping", "Stock the floor can trust"]),
        ("desk", "phone", "Field service", "Fieldnote", "A field-service app that works between signal.", "Technicians close a job when the van is still on site.", ["Offline close-out", "The office can see the van"]),
        ("screens", "users", "Education", "Batchroom", "Fees, tests, and attendance for a coaching network.", "The evening follow-up no longer depends on a chat group.", ["Fees and attendance in one place", "A list of students who are slipping"]),
        ("city", "route", "Logistics", "Dockline", "Dispatch and proof of delivery for a carrier.", "The dock sees the proof before the driver is back in the yard.", ["Routes for the day", "Proof attached to the stop"]),
        ("office", "key", "Professional services", "Ledger & Co", "A client portal with approvals and invoices.", "Clients approve work without a chain of forwarded mail.", ["Approvals in the portal", "Invoices that match the work"]),
    ]
    cards = "".join(
        f'<a class="card project" href="{e(prefix(path) + "case-studies/index.html")}">{img(path, im, title)}<div class="card-body">{icon(ic)}<p class="card-kicker">{e(sector)}</p><h3>{e(title)}</h3><p>{e(text)}</p><p class="card-more">{e(more)}</p><ul class="card-points">{"".join(f"<li>{e(b)}</li>" for b in bullets)}</ul><span class="card-link">Read the result {LINK_ARROW}</span></div></a>'
        for im, ic, sector, title, text, more, bullets in projects
    )
    opening = film(path, "Selected work", "Systems that stayed in use.", "A sample of products. Names of private clients are changed. The jobs are not.", "", "desk", "build", crumbs(path, [("Portfolio", "")]))
    body = f'''{opening}
<section class="section" style="padding-top:0"><div class="wrap portfolio">{cards}</div></section>{cta(path)}'''
    return shell(path, "Portfolio | SapporoSys", "Selected software products designed and supported by SapporoSys.", "portfolio", body)

def cases():
    path = "case-studies/index.html"
    studies = [
        ("life", "Healthcare", "Northwind Clinics", "Ward status and billing stopped living in two systems.", "Charge leakage on discharges dropped in the first quarter, because billing could see the ward board.", ["One status for the ward and the bill", "A named owner for the handoff"]),
        ("box", "Retail", "Harbour Goods", "Store managers stopped retyping orders.", "The warehouse saw the same number the shop saw, including what was already promised to a customer.", ["Orders entered once", "Stock the floor and the warehouse share"]),
        ("phone", "Field service", "Fieldnote", "Technicians closed jobs offline.", "The office stopped calling to ask where the van was. The close-out arrived when the signal returned.", ["Jobs closed on site", "Location without a phone chase"]),
    ]
    cards = "".join(card_block(h, t, ic, kicker=kicker, more=more, bullets=bullets) for ic, kicker, h, t, more, bullets in studies)
    opening = film(path, "After launch", "What changed once staff used it.", "We write these after the support window, when the polite version of the demo has worn off.", "", "meet", None, crumbs(path, [("Case studies", "")]))
    body = f'''{opening}
<section class="section" style="padding-top:0"><div class="wrap cards cards-3">{cards}</div></section>{cta(path)}'''
    return shell(path, "Case Studies | SapporoSys", "What changed for SapporoSys clients after the work shipped.", "cases", body)

def blog():
    path = "blog/index.html"
    p = prefix(path)
    cards = []
    for i, (ic, title, kicker, lead, more, length) in enumerate(BLOG):
        href = p + "blog/articles/example-article/index.html" if i == 0 else p + "blog/index.html"
        cards.append(card_block(title, lead, ic, kicker=f"{kicker}  ·  {length}", more=more, href=href))
    opening = film(path, "Studio notes", "Writing from the work.", "Short pieces on scope, handover, and the week after a release.", "", "notes", None, crumbs(path, [("Notes", "")]))
    body = f'''{opening}
<section class="section" style="padding-top:0"><div class="wrap blog-grid">{"".join(cards)}</div></section>'''
    return shell(path, "Notes | SapporoSys", "Notes from the SapporoSys studio on shipping and supporting software.", "work", body)

def article():
    path = "blog/articles/example-article/index.html"
    opening = film(path, "Scope", "What a first release should leave out.", "The smallest system that lets a real user finish a real job.", "", "laptop", None, crumbs(path, [("Notes", "blog/index.html"), ("A first release", "")]))
    body = f'''{opening}<article class="section"><div class="wrap-s article">
<div class="prose">
<p>A first release is not a smaller copy of the imagined product. It is the smallest system that lets a real user finish a real job, with the records stored somewhere other than a chat thread.</p>
<p>The features that usually need to wait are the ones that feel like completeness: every report, every role, every exception a veteran can remember. Those exceptions are real. They are also how a first version misses the season it was meant to catch.</p>
<h2>What we keep</h2>
<p>One primary job. The data that job creates. A way for a person to correct a mistake. A way to see that the job happened. Everything else is a later release with its own date.</p>
<h2>What we write down</h2>
<p>The left-out list is part of the plan, not a private compromise. Clients relax when the missing pieces have a name and a sequence, instead of hovering as guilt.</p>
<p>If you are staring at a brief that tries to include the whole company, start a conversation. We would rather propose a thinner first release than pretend the wide one will land on time.</p>
</div></div></article>'''
    return shell(path, "What a first release should leave out | SapporoSys", "How SapporoSys decides what a first software release should include.", "work", body)

def contact():
    path = "contact-us/index.html"
    opening = film(path, "Studio desk", "Write or call.", "Tell us the operation and the date that matters. A producer replies within one business day.", '<p class="fine"><a href="tel:+918041207788">+91 80 4120 7788</a> · <a href="mailto:hello@sapporosys.com">hello@sapporosys.com</a></p>', "office", "studio", crumbs(path, [("Contact", "")]))
    body = f'''{opening}<section class="section"><div class="wrap" style="max-width:760px"><div class="form-card">{form_block("Received. A producer will reply within one business day.")}</div></div></section>'''
    return shell(path, "Contact | SapporoSys", "Contact the SapporoSys studio in Bengaluru.", "contact", body)

def quote():
    path = "request-a-quote/index.html"
    opening = film(path, "A brief", "Tell us enough to price the first step.", "If the work is still fuzzy, the first step is a paid discovery, not a fixed bid built on a guess.", "", "workshop", None, crumbs(path, [("Estimate", "")]))
    body = f'''{opening}<section class="section"><div class="wrap" style="max-width:760px"><div class="form-card">{form_block("Received. We will reply with the next step, which may be a few questions or a discovery outline.")}</div></div></section>'''
    return shell(path, "Request an Estimate | SapporoSys", "Ask SapporoSys for an estimate or a discovery outline.", "contact", body)

def careers():
    path = "careers/index.html"
    roles = "".join(f'<article class="role"><div><h3>{e(t)}</h3><p>{e(d)}</p></div><p>{e(w)}</p><a class="btn btn-ink" href="#apply">Apply</a></article>' for t, w, d in ROLES)
    opening = film(path, "Hiring", "Open roles.", "We hire people who can explain a system to the person who will use it. The studio is in Bengaluru, with a few remote seats in India.", "", "team", None, crumbs(path, [("Careers", "")]))
    body = f'''{opening}
<section class="section" style="padding-top:0"><div class="wrap roles">{roles}</div></section>
<section class="section" id="apply" style="padding-top:0"><div class="wrap" style="display:grid;grid-template-columns:1fr;gap:1rem;max-width:760px"><h2>Apply</h2><div class="form-card"><form class="form" data-form><p class="form-ok">Application noted. If there is a fit, we will write back.</p><div class="fields"><label>Name <span class="req">*</span><input required name="name"></label><label>Email <span class="req">*</span><input required type="email" name="email"></label></div><label>Role <span class="req">*</span><select required name="role"><option value="">Choose a role</option>{"".join(f"<option>{e(t)}</option>" for t,_,_ in ROLES)}</select></label><label>Note <span class="req">*</span><textarea required name="note" placeholder="A few lines on work you have shipped."></textarea></label><button class="btn btn-saffron" type="submit">Send application</button></form></div></div></section>'''
    return shell(path, "Careers | SapporoSys", "Open roles at the SapporoSys studio.", "company", body)

def faqs():
    path = "faqs/index.html"
    items = "".join(f'<div class="faq-item"><button type="button" aria-expanded="false">{e(q)}</button><div><p>{e(a)}</p></div></div>' for q, a in FAQS)
    opening = film(path, "Before you brief us", "Straight answers.", "Ownership, timing, support, and where the studio actually sits.", "", "collab", None, crumbs(path, [("FAQs", "")]))
    body = f'''{opening}
<section class="section" style="padding-top:0"><div class="wrap wrap-s"><div class="faq">{items}</div></div></section>'''
    return shell(path, "FAQs | SapporoSys", "Common questions about working with SapporoSys.", "company", body)

def legal(slug):
    title, paras = LEGAL[slug]
    path = slug + "/index.html"
    prose = "".join(f"<p>{e(p)}</p>" for p in paras)
    opening = film(path, "SapporoSys", e(title), "How we handle enquiries, fees, and the work once a scope is signed.", "", "notes", None, crumbs(path, [(title, "")]))
    body = f'''{opening}<section class="section"><div class="wrap-s prose">{prose}<p>Questions: <a href="mailto:hello@sapporosys.com">hello@sapporosys.com</a>.</p></div></section>'''
    return shell(path, title + " | SapporoSys", title + " for the SapporoSys website and engagements.", "company", body)

def not_found():
    path = "404.html"
    body = film(path, "404", "That page is not on this site.", "The link may be old. The services list and the studio desk are both still here.", '<div class="actions"><a class="btn btn-saffron" href="./index.html">Back home</a><a class="btn btn-ink" href="./contact-us/index.html">Contact</a></div>', "city")
    return shell(path, "Page not found | SapporoSys", "This SapporoSys page does not exist.", "home", body)

def design():
    path = "design-system.html"
    opening = film(path, "Design system", "Ink, pearl, coral.", "Three lead colours, with slate, aqua, and pine used only for type, marks, and success states.", "", "screens")
    body = opening + '''<section class="section"><div class="wrap">
<div class="swatches">
<div class="swatch"><i style="background:#071426"></i><span>Ink navy</span></div>
<div class="swatch"><i style="background:#F6F3EE"></i><span>Pearl white</span></div>
<div class="swatch"><i style="background:#FF4B3E"></i><span>Electric coral</span></div>
<div class="swatch"><i style="background:#5C6B7A"></i><span>Slate</span></div>
<div class="swatch"><i style="background:#3EC6C0"></i><span>Aqua</span></div>
<div class="swatch"><i style="background:#1F8F6A"></i><span>Pine</span></div>
</div>
<p class="lede" style="margin-top:1.5rem">Headlines are Syne. Body text is Manrope.</p>
</div></section>'''
    return shell(path, "Design System | SapporoSys", "Color, type, and controls for the SapporoSys site.", "company", body)

def sitemap_page(paths):
    path = "sitemap.html"
    p = prefix(path)
    items = "".join(f'<li><a href="{e(p + item)}">{e(item)}</a></li>' for item in paths)
    opening = film(path, "Index", "Sitemap", "Every public page on the SapporoSys site.", "", "server")
    body = opening + f'<section class="section"><div class="wrap prose"><ul>{items}</ul></div></section>'
    return shell(path, "Sitemap | SapporoSys", "Every page on the SapporoSys site.", "company", body)

def sitemap_xml(paths):
    urls = "\n".join(f"  <url><loc>https://www.saffronsys.com/{e(item if item != 'index.html' else '')}</loc></url>" for item in paths if item != "404.html")
    return '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + "\n</urlset>\n"

def main():
    pages = {"index.html": home(), "services/index.html": services_index()}
    for item in SERVICES:
        pages[item["path"]] = service_page(item)
    for slug, data in COMPANY.items():
        active = "work" if slug == "testimonials" else "company"
        pages[slug + "/index.html"] = story_page(slug, *data, active)
    pages["locations/index.html"] = locations_index()
    for slug, name, blurb, image in LOCATIONS:
        pages[slug + "/index.html"] = location_page(slug, name, blurb, image)
    pages["portfolio/index.html"] = portfolio()
    pages["case-studies/index.html"] = cases()
    pages["blog/index.html"] = blog()
    pages["blog/articles/example-article/index.html"] = article()
    pages["contact-us/index.html"] = contact()
    pages["request-a-quote/index.html"] = quote()
    pages["careers/index.html"] = careers()
    pages["faqs/index.html"] = faqs()
    for slug in LEGAL:
        pages[slug + "/index.html"] = legal(slug)
    pages["404.html"] = not_found()
    pages["design-system.html"] = design()
    ordered = sorted(pages)
    pages["sitemap.html"] = sitemap_page(ordered)
    for rel, content in pages.items():
        dest = ROOT / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(content, encoding="utf-8")
    (ROOT / "sitemap.xml").write_text(sitemap_xml(sorted(pages)), encoding="utf-8")
    (ROOT / "robots.txt").write_text("User-agent: *\nAllow: /\nSitemap: https://www.saffronsys.com/sitemap.xml\n", encoding="utf-8")
    (ROOT / "README.md").write_text(
        "# SapporoSys\n\nStatic marketing site for SapporoSys, a software studio.\n\nOpen `index.html` in a browser, or serve this folder with any static server.\n\nPhotography and video are from Pexels and free to use, including commercially.\n",
        encoding="utf-8",
    )
    print(f"wrote {len(pages)} html pages")

if __name__ == "__main__":
    main()
