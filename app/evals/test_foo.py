from inspect_ai import Task, task
from inspect_ai.solver import Generate, Solver, TaskState, solver
from inspect_ai.dataset import MemoryDataset, Sample
from ..prompts.foo import GREET


@solver
def greet_solver() -> Solver:

    async def solve(state: TaskState, generate: Generate) -> TaskState:
        print("hello?")
        prompt = state.user_prompt
        prompt.text = GREET.format(greeting=state.input)
        await generate(state)
        return state

    return solve


@task
def eval_foo() -> Task:
    return Task(
        name="foo",
        dataset=MemoryDataset(samples=[Sample(input="hello", target="hello world!")]),
        plan=[greet_solver()],
    )


def test_foo():
    print("test_foo")
