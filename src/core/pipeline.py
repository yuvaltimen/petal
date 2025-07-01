from src.core.context import PipelineContext
from src.core.utils import is_dag, topological_sort


class Pipeline(PipelineContext):
    def __init__(self, pipeline_name: str):
        super().__init__()
        self.name = pipeline_name

        def validate(self):
            if not is_dag(self.edges):
                raise ValueError("Pipeline contains a cycle")

        def run(self):
            self.validate()

            execution_order = topological_sort(self.edges)
            context = {}

            print(f"[RUNNING] Pipeline '{self.name}'")

            for node_id in execution_order:
                node = self.nodes[node_id]
                inputs = [context[parent.node_id] for parent in node.upstream]
                print(f"  - Executing node: {node_id}")
                result = node.process(*inputs)
                context[node_id] = result
