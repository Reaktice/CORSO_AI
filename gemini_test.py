import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyCLH-tfMK0VwCOccixGmV_raPYle6UOr7s")

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "create an ai essay",
      ],
    },
    {
      "role": "model",
      "parts": [
        "## The Unfolding Narrative of Artificial Intelligence: Promise, Peril, and the Path Forward\n\nArtificial intelligence (AI) is no longer a futuristic fantasy; it's a rapidly evolving reality weaving itself into the fabric of our lives. From the mundane – spam filters and personalized recommendations – to the extraordinary – medical diagnoses and autonomous vehicles – AI's influence is undeniable and accelerating. This essay will explore the multifaceted nature of AI, examining its transformative potential alongside the ethical and societal challenges it presents.\n\nThe promise of AI is immense.  Its ability to process vast datasets and identify patterns invisible to the human eye holds the key to solving some of humanity's most pressing problems. In healthcare, AI-powered diagnostic tools can detect diseases earlier and more accurately, leading to improved treatment outcomes. In climate science, AI can analyze complex environmental data to predict and mitigate the effects of climate change.  In manufacturing, AI-driven automation can increase efficiency and productivity while reducing human error. The potential applications are virtually limitless, promising a future of increased efficiency, innovation, and overall well-being.\n\nHowever, this promising narrative is interwoven with significant perils.  One major concern centers around bias. AI algorithms are trained on data, and if that data reflects existing societal biases – be it racial, gender, or socioeconomic – the AI system will inevitably perpetuate and even amplify those biases. This can lead to discriminatory outcomes in areas like loan applications, hiring processes, and even criminal justice, exacerbating existing inequalities.  Furthermore, the increasing autonomy of AI systems raises questions about accountability. When an autonomous vehicle causes an accident, who is responsible?  The programmer? The manufacturer? The owner?  Establishing clear lines of responsibility is crucial to prevent misuse and ensure ethical conduct.\n\nThe issue of job displacement is another critical concern. As AI-powered automation becomes more sophisticated, it's likely to displace workers in various sectors, potentially leading to widespread unemployment and social unrest.  Addressing this challenge requires proactive measures, such as investing in retraining programs and exploring alternative economic models that can accommodate a workforce increasingly augmented by AI.\n\nThe path forward requires a multi-pronged approach.  Firstly, fostering ethical AI development is paramount.  This involves creating robust guidelines and regulations that prioritize fairness, transparency, and accountability.  Research into explainable AI (XAI) – systems that can explain their decision-making processes – is crucial for building trust and addressing concerns about bias. Secondly, promoting digital literacy and education is essential to equip individuals with the skills necessary to navigate the changing landscape of work and technology.  Finally, fostering open dialogue and collaboration between researchers, policymakers, and the public is vital to ensure that the development and deployment of AI align with societal values and benefit all of humanity.\n\nIn conclusion, AI represents a powerful technology with the potential to revolutionize our world.  However, realizing its full potential while mitigating its risks requires careful consideration of its ethical implications and proactive measures to address the potential challenges.  Only through a concerted effort to develop and deploy AI responsibly can we ensure that this transformative technology serves humanity's best interests.\n",
      ],
    },
  ]
)

keyboardInput= input("Inserisci il tuo prompt: ")
response = chat_session.send_message(keyboardInput)

print(response.text)