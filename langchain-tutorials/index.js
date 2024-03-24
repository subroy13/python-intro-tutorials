import { ChatAnthropic } from '@langchain/anthropic';
import { PromptTemplate } from '@langchain/core/prompts';
import { Runnable } from '@langchain/core/runnables';
import { StringOutputParser } from '@langchain/core/output_parsers';

import 'dotenv/config';

const prompt = PromptTemplate.fromTemplate(`Tell me a joke about {subject}`);

const model = new ChatAnthropic({
    anthropicApiKey: process.env?.CLAUDE_API_KEY,
    modelName: "claude-3-haiku-20240307"
});

const functionSchema = [
    {
      name: "joke",
      description: "A joke",
      parameters: {
        type: "object",
        properties: {
          setup: {
            type: "string",
            description: "The setup for the joke",
          },
          punchline: {
            type: "string",
            description: "The punchline for the joke",
          },
        },
        required: ["setup", "punchline"],
      },
    },
];

const chain = prompt.pipe(
    model.bind({
      functions: functionSchema,
      function_call: { name: "joke" },      // force it to use a specific function call
        // Note that, your function Schema may contain multiple function schema, but
        // only restrict to a particular function to use
    })
);

const result = await chain.invoke({ subject: "bears" });
        // works with openai, but not with Claude haiku, as function calling is not present
console.log(result);


