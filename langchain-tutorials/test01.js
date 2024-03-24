import { ChatAnthropic } from '@langchain/anthropic';
import { PromptTemplate } from '@langchain/core/prompts';
import { RunnableSequence } from '@langchain/core/runnables';
import { StringOutputParser } from '@langchain/core/output_parsers';

import 'dotenv/config';

const prompt = PromptTemplate.fromTemplate("Tell me 5 {items} about {things} as a numbered list.");

const model = new ChatAnthropic({
    anthropicApiKey: process.env?.CLAUDE_API_KEY,
    modelName: "claude-3-haiku-20240307"
});

const parser = new StringOutputParser();

/**
 * Pipe tells you how to run a LLM chain
 *      - Prompt => LLM Model => Final Parser
 */
const chain = prompt.pipe(model.bind({
    stop: ["4. "]       // stop at the 4th point.
})).pipe(parser);

// you can also do the following
// const chain = RunnableSequence.from([
//     prompt,
//     model,
//     parser
// ]);


const result = await chain.invoke({
    items: "facts",
    things: "Eiffel Tower"
});

console.log(result);