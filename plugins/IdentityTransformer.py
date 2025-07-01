from typing import Any

from core.transformer import Transformer


class IdentityTransformer(Transformer):
    def transform(self, data: Any) -> Any:
        print(f'IdentityTransformer: {data}')
        return data
