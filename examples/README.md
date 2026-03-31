# Example Inputs / 样例输入

## 中文说明

这个目录保存的是 **仓库测试用的样例 PDF**。

它们用于：

- 复现实验
- 重建 example paper packages
- 回归测试和验证

它们**不是**普通用户运行 skill 时必须使用的固定目录。

如果你只是想处理一篇自己的论文，直接把本地 PDF 路径交给 `paperer` 即可，不需要先复制到这里。

## English Explanation

This folder stores **example PDFs for repo-side testing**.

They are used for:

- reproducible examples
- rebuilding committed example paper packages
- regression checking and validation

They are **not** a required runtime location for normal users.

If you simply want to process your own paper, pass your local PDF path directly to `paperer`. There is no need to copy the file into this folder first.

## Included Example PDFs / 当前样例 PDF

- `Tan2026.pdf`
- `Simulating Particle Dispersions in Nematic Liquid-Crystal Solvents.pdf`

## Repo Test Flow / 仓库测试流程

```text
examples/papers/*.pdf
  -> scripts/rebuild_<slug>_bundle.py
  -> output/papers/<paper-slug>/
  -> scripts/validate_paper_bundle.py
```

## Production Flow / 实际使用流程

```text
/absolute/path/to/your-paper.pdf
  -> paperer
     -> paper-package-runner
        -> literature-summary
           -> paper-asset-extraction
  -> output/papers/<paper-slug>/
```
