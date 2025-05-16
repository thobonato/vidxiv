# vidXiv: Paper to Video

## 1. Paper Ingestion
- **Input**: Upload PDF or enter DOI  
- **Parse**: Extract raw text using tools like `pdfplumber` or `PyMuPDF`  
- **Optional**: Pull metadata from arXiv or Semantic Scholar for added context

---

## 2. Section Mapping (LLM-Orchestrated Storyboard)
- **Goal**: Identify key storytelling beats  
- **LLM Breakdown**: Auto-split into:
  - Hook  
  - Intro (big picture)  
  - Methods (visualizable logic)  
  - Results (key outcomes)  
  - Conclusions (insight)  
  - Takeaways + Further Reading  
- **Customizable**: Adjust style/depth based on audience (e.g., high schooler vs PhD)

---

## 3. Storyboard Design
For each section:
1. **Narration Draft**  
   - Bullet-point narration: clear, concise, and pedagogical  
2. **Visual Plan**  
   - Match each bullet with a visual: diagram, animation, data chart  
   - Specify style and medium (e.g. ManimCE, D3, schematic)

> ⚠️ **Rule**: Write narration *first*, then design visuals — not the other way around.

---

## 4. Asset Generation

### a. Voiceover
- Finalize script  
- Generate audio via ElevenLabs, Bark, or OpenVoice

### b. Visuals
- Use LLM (e.g. Gemini 1.5 Pro) to:
  - Translate visual prompts to object-oriented **ManimCE** code  
  - Auto-debug + render scenes  
  - Second-pass refinement via frame-by-frame LLM QA  

---

## 5. Video Assembly
- Stitch visuals + voice using `moviepy` or `ffmpeg`  
- Add transitions, title cards, intro/outro, lower-thirds  
- Optional: Add music bed, captions, or dynamic text

---

## 6. Export & QA
- **Output**: Final MP4  
- **Review**: Manual watch-through or LLM-based QA for pacing, clarity  
- **Delivery**: Publish to platform or return to user

---

## Coming Soon
- Extract diagrams, figures, and tables from PDFs  
- Auto-citation + source credits  
- Style presets: “3Blue1Brown,” “Kurzgesagt,” “CrashCourse”  
- Auto-upload to YouTube (title, thumbnail, description)  
- Auto-generate summary notes or viewer quiz

---

## Stretch Vision
- 🔁 Feedback loops from viewers → LLM tuning for better future videos  
- 📚 Multi-paper “State of the Field” synthesis videos  
- 🤝 Researcher-facing tool: upload your paper → get editable video draft