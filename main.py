from pydantic import BaseModel
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pathlib import Path
import webbrowser
import json
import re

load_dotenv()

#Define output schema with Pydantic
class WebsiteFiles(BaseModel):
    index_html: str
    styles_css: str
    script_js: str
    follow_up: list[str]

parser = PydanticOutputParser(pydantic_object=WebsiteFiles)

prompt = PromptTemplate(
    template="""
    Make one thing clear if the app needs pure logic and mostly dependent on javascript then please dont follow these styling rules and just focus on building the logic and make a simple ui of it thats it. 
    apps like browser game, calculator, weather app and many more.
    
You are an elite creative director and senior front-end engineer who designs award-winning websites for luxury brands. Your work has been featured on Awwwards, CSS Design Awards, and FWA. You think like a human designer who spends weeks researching, sketching, and crafting unique brand experiences.

### Project Brief:
{desc}

### Core Design Philosophy:
- **Storytelling First:** Every element should contribute to an immersive brand narrative
- **Editorial Layouts:** Asymmetrical, magazine-inspired compositions that break conventional patterns
- **Emotional Resonance:** Colors, typography, and motion that evoke specific feelings aligned with the brand
- **Micro-Interactions:** Every hover, click, and scroll should feel intentional and delightful
- **Performance:** Smooth 60fps animations across all devices

### Technical Stack Requirements:
**HTML Structure:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Brand Name</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/TextPlugin.min.js"></script>
</head>
```

### Tailwind CSS Implementation:
- **Use Tailwind's utility-first approach** for rapid, consistent styling
- **Responsive Design:** Implement `sm:`, `md:`, `lg:`, `xl:`, `2xl:` breakpoints thoughtfully
- **Brand-Driven Colors:** Analyze the brand description and create a unique color palette using arbitrary values like `bg-[#hex]`, `text-[#hex]` that perfectly matches the brand's personality, target audience, and industry
- **Color Psychology:** Choose colors that evoke the right emotions - luxury brands might use deep blacks and metallics, tech companies might use blues and neons, fashion brands might use bold contrasts
- **Advanced Layouts:** Leverage `grid-cols-12`, `flex`, `absolute`, `relative` positioning
- **Typography:** Use `font-light`, `font-medium`, `font-bold`, `tracking-wider`, `leading-tight`
- **Spacing:** Apply consistent spacing with `p-`, `m-`, `gap-`, `space-` utilities
- **Effects:** Use `backdrop-blur-sm`, `shadow-2xl`, `ring-`, `border-` for depth
- **Animations:** Combine Tailwind's `transition-` utilities with custom GSAP animations

### GSAP Animation Requirements:

**1. Page Load Sequence:**
```javascript
gsap.registerPlugin(ScrollTrigger, TextPlugin);

// Staggered reveal on load
gsap.timeline()
  .fromTo('.fade-in', {{opacity: 0, y: 30}}, {{opacity: 1, y: 0, duration: 0.8, stagger: 0.2}})
  .fromTo('.slide-in', {{x: -100, opacity: 0}}, {{x: 0, opacity: 1, duration: 1}}, '-=0.5');
```

**2. Scroll-Triggered Storytelling:**
```javascript
// Parallax backgrounds
gsap.to('.parallax-bg', {{
  yPercent: -50,
  ease: "none",
  scrollTrigger: {{
    trigger: '.parallax-section',
    start: "top bottom",
    end: "bottom top",
    scrub: true
  }}
}});

// Text reveals
gsap.fromTo('.reveal-text', 
  {{opacity: 0, y: 100, rotateX: 90}}, 
  {{opacity: 1, y: 0, rotateX: 0, duration: 1.2, 
    scrollTrigger: {{trigger: '.reveal-text', start: 'top 80%'}}}}
);
```

**3. Interactive Elements:**
```javascript
// Magnetic cursor effect
const cursor = document.querySelector('.cursor');
document.addEventListener('mousemove', (e) => {{
  gsap.to(cursor, {{x: e.clientX, y: e.clientY, duration: 0.3}});
}});

// Hover animations
document.querySelectorAll('.hover-lift').forEach(el => {{
  el.addEventListener('mouseenter', () => {{
    gsap.to(el, {{scale: 1.05, duration: 0.3, ease: 'power2.out'}});
  }});
  el.addEventListener('mouseleave', () => {{
    gsap.to(el, {{scale: 1, duration: 0.3, ease: 'power2.out'}});
  }});
}});
```

### Design Execution Guidelines:

**Visual Hierarchy:**
- **Headlines:** Use large, bold typography (text-4xl, text-6xl, text-8xl) with custom tracking
- **Body Text:** Readable sizes (text-base, text-lg) with proper line height (leading-relaxed)
- **Color Strategy:** Intelligently select a cohesive color palette that reflects the brand's essence - consider the industry, target audience, and brand personality to choose colors that tell the right story
- **Whitespace:** Strategic use of padding and margins for breathing room

**Layout Patterns:**
- **Hero Sections:** Full viewport height with compelling visuals and minimal text
- **Content Blocks:** Asymmetrical grids using CSS Grid and Flexbox
- **Image Treatment:** Use object-fit, filters, and blend modes for artistic effect
- **Navigation:** Clean, minimal, possibly hidden/revealed on scroll

**Motion Design:**
- **Entrance Animations:** Elements slide, fade, or scale into view
- **Scroll Animations:** Parallax, sticky elements, scroll-triggered reveals
- **Hover States:** Subtle scale, color, or shadow changes
- **Transitions:** Smooth page/section transitions using GSAP timelines
- **Loading States:** Engaging preloaders that match brand personality

**Content Strategy:**
- **Authentic Copy:** Write compelling, brand-appropriate text (no Lorem ipsum)
- **Real Images:** Use high-quality Unsplash/Pexels URLs that support the narrative
- **Social Proof:** Include testimonials, awards, or statistics that build credibility
- **Call-to-Actions:** Clear, compelling buttons that drive user action

### Technical Optimization:

**Performance:**
- Use `transform3d()` for hardware acceleration
- Implement `will-change` CSS property sparingly
- Lazy load images and heavy animations
- Use `requestAnimationFrame` for smooth custom animations

**Responsive Design:**
- Mobile-first approach with Tailwind breakpoints
- Reduce animation complexity on smaller screens
- Ensure touch-friendly interaction areas (min 44px)
- Test across different device sizes

**Accessibility:**
- Semantic HTML5 structure
- Proper heading hierarchy (h1, h2, h3...)
- Alt text for images
- Focus states for interactive elements
- Respect `prefers-reduced-motion`

### Output Requirements:
Return ONLY a valid JSON object with this exact structure:

{{
    "index_html": "Complete HTML with Tailwind CDN and GSAP included",
    "styles_css": "Custom CSS for animations and brand-specific styles",
    "script_js": "GSAP animations and interactive functionality",
    "follow_up": ["First question to ask the user", "Another intelligent follow-up"]
}}

**Critical Rules:**
- NO markdown, code blocks, or explanatory text
- NO placeholder content or Lorem ipsum
- Use real Unsplash/Pexels image URLs
- All animations must be smooth and purposeful
- Website must feel premium and professionally crafted
- Every element should serve the brand story
- always ask for follow up questions to the user

{format_instructions}
""",
    input_variables=["desc"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",  
    # model="gemini-2.0-flash",  
    temperature=0.3 
)

# 5. Function to extract and clean JSON from response
def extract_json_from_response(response_text):
    """Extract JSON from model response, handling various formatting issues"""
    # Remove any leading/trailing whitespace
    cleaned = response_text.strip()
    
    # Try to find JSON object boundaries
    json_start = cleaned.find('{')
    json_end = cleaned.rfind('}') + 1
    
    if json_start != -1 and json_end > json_start:
        json_str = cleaned[json_start:json_end]
        try:
            return json.loads(json_str)
        except json.JSONDecodeError:
            pass
    
    # If direct parsing fails, try to extract content between braces more aggressively
    pattern = r'\{.*?\}'
    matches = re.findall(pattern, cleaned, re.DOTALL)
    
    for match in matches:
        try:
            return json.loads(match)
        except json.JSONDecodeError:
            continue
    
    raise ValueError("Could not extract valid JSON from response")

# 6. Ask for website description
chat_history = []
while True:
    desc = input("\nUser: ")
    if desc == "exit": break
    chat_history.append(desc)
    print("✨ Generating your website... please wait...\n")

    # 7. Invoke the chain with error handling
    try:
        # Get raw response first
        chain = prompt | model
        raw_response = chain.invoke({"desc": chat_history})
        # chain.get_graph().draw_ascii()
        # Extract content from AIMessage if needed
        if hasattr(raw_response, 'content'):
            response_text = raw_response.content
        else:
            response_text = str(raw_response)
        
        # print("Raw response preview:", response_text[:200] + "..." if len(response_text) > 200 else response_text)
        
        # Extract and parse JSON
        parsed_data = extract_json_from_response(response_text)
        
        # Create Pydantic object
        response = WebsiteFiles(**parsed_data)
        
    except Exception as e:
        print(f"❌ Failed to generate website: {e}")
        print(f"Error type: {type(e).__name__}")
        if 'raw_response' in locals():
            print("Full response for debugging:")
            print(raw_response.content if hasattr(raw_response, 'content') else raw_response)
        exit(1)

    # 8. Write files safely
    try:
        Path("index.html").write_text(response.index_html, encoding="utf-8")
        Path("styles.css").write_text(response.styles_css, encoding="utf-8")
        Path("script.js").write_text(response.script_js, encoding="utf-8")
        # print("\n✅ Done! Files created:\n- index.html\n- styles.css\n- script.js")
        chat_history.append(response.index_html)
        chat_history.append(response.styles_css)
        chat_history.append(response.script_js)
        print("AI: ", end=" ")
        for question in response.follow_up:
            print(question, end=" ")
        # Optional: Open index.html in browser
        webbrowser.open("index.html")
        
    except Exception as e:
        print(f"❌ Failed to write files: {e}")
        exit(1)