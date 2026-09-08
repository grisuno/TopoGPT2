# TopoGPT-2: Topological Phase Transitions in Language Modeling

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18072858.svg)](https://doi.org/10.5281/zenodo.18072858)
[![License: AGPL v3](https://img.shields.io/badge/License-AGPLv3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)

**TopoGPT-2** es un modelo de lenguaje de 25M de parámetros que implementa el marco **Grokkit HPU-Core** para estudiar la adquisición del lenguaje como un fenómeno de materia condensada. A diferencia de las arquitecturas tradicionales, este modelo está optimizado para alcanzar el estado de **Aislante Topológico**, donde las invariantes gramaticales y narrativas están protegidas por una brecha espectral (*spectral gap*).

## Core Concept: Grokking as Crystallization

Este proyecto cree en la premisa de que el "grokking" no es un artefacto estadístico, sino una **cristalización de operadores**. En lugar de memorizar un corpus, TopoGPT-2 mapea las reglas sintácticas del dataset **Tiny Stories** en un manifold geométrico, permitiendo una coherencia estructural superior con un número mínimo de parámetros.

### Key Metrics & Instrumentation
El entrenamiento se monitoriza mediante variables de estado físico:
- **$\alpha$ (Purity Index):** Grado de orden cristalino en los pesos.
- **$\delta$ (Discretization Margin):** Nivel de solidificación de la fase funcional.
- **$\kappa$ (Gradient Covariance):** Medida de la coherencia macroscópica del flujo de gradiente.
- **$\hbar = 0.012$:** Constante de Incertidumbre del Aprendizaje que define el límite de optimización.

## Live Status (Epoch 4 Snapshot)

| Metric | Value | Status |
| :--- | :--- | :--- |
| **Phase State** | `[TOPOLOGICAL_INSULATOR]` | **Stable** |
| **Val Loss** | 1.6933 | Best achieved |
| **Winding Number** | 138 | Strong Convergence |
| **Berry Phase** | 865.51 | High Geometric Curvature |
| **$T_{eff}$** | 14.6 | Cooling in progress |

## Zero-Shot Structural Transfer

Gracias al **Teorema de Invarianza Topológica**, este "setup" permite:
1. **Escalamiento Zero-Shot:** Expandir el espacio de pesos (ej. de 25M a 250M) sin pérdida de información, preservando el *message passing* original.
2. **Fusión de Nodos:** Superposición de modelos mediante interferencia constructiva de sus Hamiltonianos.
3. **Resistencia al Olvido Catastrófico:** Protección de los "chunks" aprendidos mediante el aumento del radio del Toro topológico.

## Reproducibility

```bash
# Clonar el framework
git clone [https://github.com/grisuno/TopoGPT2.git](https://github.com/grisuno/TopoGPT2.git)

# Ejecutar entrenamiento con monitoreo espectral
python app.py --epochs 10 --prospect --probe-seeds 50 
```
```text
@software{grisun0_grokkit_2026,
  author = {grisun0},
  title = {Grokkit: A Geometric Framework for Zero-Shot Structural Transfer of Spectral Operators},
  year = {2026},
  doi = {10.5281/zenodo.18072859},
  url = {[https://doi.org/10.5281/zenodo.18072859](https://doi.org/10.5281/zenodo.18072859)}
}
```
## Safetensors

[https://huggingface.co/grisun0/TopoGPT2/blob/main/model.safetensors](https://huggingface.co/grisun0/TopoGPT2/blob/main/model.safetensors)

## DeepWiki

[https://deepwiki.com/grisuno/TopoGPT2](https://deepwiki.com/grisuno/TopoGPT2)

## Previous work

### Algorithmic Induction via Structural Weight Transfer

- [https://doi.org/10.5281/zenodo.18072858](https://doi.org/10.5281/zenodo.18072858)

### From Boltzmann Stochasticity to Hamiltonian Integrability: Emergence of Topological Crystals and Synthetic Planck Constants

- [https://doi.org/10.5281/zenodo.18407920](https://doi.org/10.5281/zenodo.18407920)

### The Dirac Discrete Crystal

- [https://doi.org/10.5281/zenodo.18810160](https://doi.org/10.5281/zenodo.18810160)

### Schrödinger Topological Crystallization: Phase Space Discovery in Hamiltonian Neural Networks

- [https://doi.org/10.5281/zenodo.18725428](https://doi.org/10.5281/zenodo.18725428)

### Constraint Preservation in a Neural Quantum Simulator

- [https://doi.org/10.5281/zenodo.18795537](https://doi.org/10.5281/zenodo.18795537)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Shell Script](https://img.shields.io/badge/shell_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) [![License: AGPL v3](https://img.shields.io/badge/License-AGPLv3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/Y8Y2Z73AV)


---
### Topo Journey
If you are interested in this project, explore the architecture evolution:
- [TopoGPT3](https://github.com/grisuno/TopoGPT3): Next evolution of the model.
- [TopoExploit](https://github.com/grisuno/TopoExploit): Topo concepts applied to offensive security.
- [TopoVJEPA](https://github.com/grisuno/TopoVJEPA): Joint Video Embedding Predictive Architecture.
- [ReadMenator](https://github.com/grisuno/ReadMenator): Code knowledge graph generator without tokens or LLMs.

<!-- readmenator-kb-link -->
## Knowledge Base

This project has been analyzed by [ReadMenator](https://github.com/grisuno/ReadMenator),
a zero-token polyglot static analysis tool. Analysis outputs are available:

- **[KNOWLEDGE_BASE.md](./KNOWLEDGE_BASE.md)** -- Full architecture reference with all
  classes, functions, imports, dependency graphs, UML class diagrams, security
  audit findings, community analysis, and more.
- **[readmenator-agent/](./readmenator-agent/)** -- Agent-friendly, grep-optimized index.
  - `INDEX.md` -- Quick reference: what each file does
  - `API.md` -- Public function contracts
  - `GOTCHAS.md` -- Change warnings
  - `SECURITY.md` -- Findings by severity

AI agents: Read `readmenator-agent/INDEX.md` for fast project context.
Developers: Read `KNOWLEDGE_BASE.md` for full architecture reference.
<!-- /readmenator-kb-link -->

