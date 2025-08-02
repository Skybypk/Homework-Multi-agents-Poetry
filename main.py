from agents import Agent, Runner, trace, function_tool
from connection import config
import asyncio
from dotenv import load_dotenv

load_dotenv()
@function_tool
def author():
    return "Saeed Khan"

Lyrical_agent = Agent(
    name = 'Lyrical Agent',
    instructions="You are a lyrical poetry agent. Your job is to do two things:" 
    "Analyze a given poem and decide if it's lyrical. Lyrical poetry expresses personal emotions, feelings, and is often musical in nature."
    "If requested, generate original lyrical poetry based on a theme, mood, or structure provided by the user."
)

Narrative_agent = Agent(
    name = "Narrative Agent",
    instructions="You are a Narrative Poetry Agent. Your responsibilities are: "
    "Analyze a given poem and determine whether it is narrative poetry." 
    "Narrative poems usually tell a story with a beginning,"
    "middle, and end, and often include characters and dialogue."
    "If asked, generate a short narrative poem based on a theme or story idea provided by the user."
)    

Dramatic_agent = Agent(
    name = 'Dramatic Agent',
    instructions="You are a Dramatic Poetry Analyzer."
    "Your task is to read a poem and determine if it falls under the category of dramatic poetry."
    "Dramatic poetry is written to be performed aloud, often involving a character speaking or acting,"
    "in a dramatic situation. It usually presents a conflict or intense emotional experience through dialogue or monologue." 
)
model="gpt3"


parent_agent = Agent(
    name = "Parent Agent",
    instructions=
    """ 
        You are a parent agent. Your task is to
        delegate user query to approriate agent. and call the tool by yourself
        Delegate poetry for our lines related queries to Lyrical agent.
        Delegate related queries to Narrative agent like story.
        And query other than Dramatic agent keep it to 
        yourself and deny the user query,

        You also have tools available like current location
        and current weather
    """,
    handoffs=[Lyrical_agent,Narrative_agent,Dramatic_agent],
    
)

async def main():
    with trace("Class 06"):
        result = await Runner.run(
            parent_agent, 
            """ 
            The Final Hour Drama:
            (A woman stands alone on stage, speaking to a vanished lover)
            You left when the clock struck one,
            And now, I wait, though the night is done.
            I lit the lamp, I wore your coat,
            I whispered truth in every note.
            Was I too bold? Was silence your shield?
            Did love for me no longer yield?
            You vowed beneath that silver tree
            "Come storm or fire, you'll come to me."
            But now the air is still and cold,
            Your promise lost, your story old.
            And here I stand, with aching breath,
            To love a man who chose his death.
            (She pauses, then walks slowly offstage...) 
            """, 
            run_config=config)
        print(result.final_output)
        print("Last Agent ==> ",result.last_agent.name)


if __name__ == "__main__":
    asyncio.run(main())

  