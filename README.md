# Seeing Life Beneath the Surface: A Data-Driven Narrative on Cetacean Protection and Public Responsibility

**[Please insert your Teaser Figure here. This should be a high-res PNG (1600x900px) from your /assets/ folder that visually captures the essence of your project, such as a collage of your website, AR experience, and a whale.]**

## Abstract

This visualization project explores global cetacean protection through an interactive narrative website designed for learning, reflection, and public engagement. Our primary audience includes museum visitors, youth learners, and the general public, aiming to transform complex environmental data into a personal and understandable experience. The project guides users through the topic starting with "Sophie’s Story," a narrative that establishes an emotional connection before introducing data-driven exploration. Core features include AR-triggered individual whale stories accessible via QR codes and global visualizations of cetacean distribution, marine parks, conservation organizations, and legal protection timelines. An optional life-stage game, "A Beluga’s Life," is proposed to further deepen engagement. By mapping cultural attitudes toward whales to contextualize policy differences, the project turns abstract environmental issues into situated learning experiences. Inspired by field trips to science museums, this prototype aims to foster critical reflection, ethical awareness, and informed advocacy for cetacean protection, providing anticipated educational and social value by connecting personal stories with global ecological systems.

## Academic Professionalism

**Disclaimer:** This InfoVis project is for submission to INFOSCI 301 Data Visualization and Information Aesthetics Spring 2026, instructed by Professor Luyao Zhang at Duke Kunshan University. This proposal and the associated prototype are created for educational purposes to explore the intersection of data visualization, narrative storytelling, and community-based learning.

**Acknowledgments:** We extend our sincere gratitude to Professor Luyao Zhang for her guidance on the principles of data visualization and information aesthetics, which form the foundation of this work. We also thank our peer classmates in INFOSCI 301 for their valuable feedback during the design process. Our field trips to the Jiading District Urban Planning Exhibition Hall, the Fengxian Waving Cube Sci-Fi Immersive Museum, and the Kunshan Museum of Chinese Opera Genres (Kunqu Opera Living Heritage) provided critical inspiration for our project's spatial, interactive, and narrative frameworks. Finally, we acknowledge the China Cetacean Alliance (CCA) and the contributors to Ceta-Base for their rigorous data collection and public advocacy, which make projects like this possible.

**Contribution to SDG Goals:**
This project directly supports the following United Nations Sustainable Development Goals (SDGs):
- **SDG 4: Quality Education.** The project transforms complex, expert-led investigative reports into accessible, interactive narratives. By designing for museum visitors and youth learners, it promotes situated learning and critical reflection on environmental issues, fostering a more informed and engaged public.
- **SDG 14: Life Below Water.** By visualizing the global context of cetacean captivity, conservation efforts, and legal protections, the project raises public awareness about the threats to marine life. It aims to translate data into empathy and advocacy, contributing to the conservation and sustainable use of oceans and marine resources.

**Statement of Accessibility:**
In alignment with SIGCHI's guidelines for inclusive design, this project is committed to accessibility. The final interactive website and all related materials are being developed with consideration for diverse users. The source code, data processing scripts, and project documentation are openly available in our GitHub repository. The datasets used, or links to the original public datasets, are accessible via our Hugging Face repository to promote transparency and reproducibility.
- **GitHub Repository:** [Sunny156-hungry/Arctic_voice](https://github.com/Sunny156-hungry/Arctic_voice)
- **Hugging Face Dataset:** [https://huggingface.co/datasets/tccc7777/Arctic_Voice_Infosci301](https://huggingface.co/datasets/tccc7777/Arctic_Voice_Infosci301)
- **Interactive Demo:** **[Please insert the URL to your live interactive demo here once it is deployed.]**

**Keywords:** Information visualization; geospatial storytelling; community-based learning; cetacean conservation; data ethics; interactive narrative; public engagement; situated learning.

## Embedded Multimedia

### Teaser Video
**[Please embed your teaser video here. This can be done by uploading the video to the /assets/ folder and embedding it using an HTML5 video tag, or by uploading it to a platform like YouTube or Vimeo and embedding the link. The video should be ~3 minutes long, covering your scientific communication, a user walkthrough, and team acknowledgments.]**

Example using an image linked to the video file:
[![Watch the Teaser Video](assets/teaser_video_thumbnail.jpg)](assets/teaser_video.mp4)

### Project Poster
**[Please embed a preview of your final project poster here. This could be a high-resolution image (e.g., poster_preview.png) stored in your /assets/ folder, linked to a PDF version or your Canva workspace.]**

[View the project poster on Canva](**[Insert your Canva workspace link here]**)

## Project Value and Community Impact

This project serves public cultural audiences, including museum visitors, students, and learners who typically encounter cetaceans as spectacles in aquariums or media. Our goal is to reposition whales and dolphins within their full ecological, legal, and cultural contexts, fostering active and reflective learning. The design directly supports educators and advocates like the China Cetacean Alliance (CCA) by translating their research into accessible public knowledge. Insights from our field trips were foundational: the Jiading Planning Exhibition Hall inspired our map-based global overview, the Waving Cube Sci-Fi Museum influenced our game-like interactive elements such as AR stories, and the Kunshan Museum of Chinese Opera Genres showed us the power of personal storytelling, leading to the creation of "Sophie’s Story."

## Data Sources, Processing, and Governance

Our project is built upon a foundation of transparency and reproducibility. The primary dataset is manually extracted from the **China Cetacean Alliance (CCA) Investigative Dataset (2019–2024)**. This data includes facility names, locations, species held, and welfare incident records. All raw and processed data, along with metadata schemas documenting variables and sources, are stored in the `/data/` directory. The data processing pipeline is fully documented and replicable, involving PDF extraction, cleaning with Python scripts, and version-controlled hosting on GitHub. Our data governance principles ensure privacy by using only facility-level aggregation and clearly marking narrative components like "Sophie’s Story" as distinct from verified data. Inclusivity is reflected in our bilingual labeling and the integration of diverse data perspectives.

**[You can include your flowchart images here, e.g., Figure 2 and Figure 3 from your report, to visually explain your process.]**
![Data Processing Workflow](assets/Figure_2_data_workflow.png)
![Data Merging Flowchart](assets/Figure_3_merging_flowchart.png)

## Visualization Tools, Design Flow, and Innovation

The project is implemented as an interactive narrative website. The design flow guides the user from story to data to interaction and finally to reflection. It begins with "Sophie’s Story" to establish emotional context, then transitions into data-driven modules like global maps and timelines. AR-triggered stories and a potential life-stage game provide deeper, experiential learning. For instance, our Streamlit dashboard translates dataset attributes like `year` and `venue_name` into clear visual encodings such as bar charts and KPI cards, ensuring the visual meaning is directly traceable to the underlying data.

Our work is inspired by the detailed but expert-focused reports of the China Cetacean Alliance and existing public narratives that often frame cetaceans primarily as welfare subjects. We innovate by creating a non-linear, interactive system that allows the public to connect individual whale stories with broader ecological systems. This approach is informed by recent research positioning cetaceans as ecosystem engineers crucial for ocean nutrient cycling and climate regulation. Our project thus acts as a critical translational medium, bridging complex marine ecology research, civic education, and ethical public engagement, making scientific insights accessible to a non-expert audience.

**[Please insert your Design Flow diagram and Streamlit dashboard screenshot here, as referenced in your report (Figures 4 and 5).]**
![Project Design Flow](assets/Figure_4_design_flow.png)
![Streamlit Dashboard Interface](assets/Figure_5_dashboard.png)

## Repository Structure
