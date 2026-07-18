# Shop Tracker

Suivi communautaire des prix d'un shop de serveur Minecraft, alimenté par les pull requests des joueurs.

## Mise en place (5 minutes)

1. Crée un repo GitHub (public, pour que les joueurs puissent proposer des PR) et pousse ces fichiers dedans.
2. Va dans **Settings → Pages** du repo, et choisis "Deploy from branch" → branche `main` → dossier `/ (root)`.
3. Ton site sera dispo à `https://<ton-pseudo>.github.io/<nom-du-repo>/` en quelques minutes.
4. Partage le lien du repo aux joueurs, avec le fichier `CONTRIBUTING.md` comme mode d'emploi.

## Structure

```
data/prices.json                     → les relevés de prix (item, prix, date)
scripts/validate.py                  → validation automatique du format
.github/workflows/validate-prices.yml → tourne à chaque pull request
index.html                           → page d'affichage (graphique + sélecteur)
CONTRIBUTING.md                      → mode d'emploi pour les joueurs
```

## Pour aller plus loin

- **Auto-merge** : ajouter `automerge` via une Action type `pascalgn/automerge-action` si tu veux que les PR valides se fusionnent sans que tu cliques.
- **Bot Discord** : si tu veux éviter complètement le passage par GitHub, ton bot Discord existant pourrait avoir une commande `/prix Diamant 130` qui ouvre la PR automatiquement via l'API GitHub (avec un token en secret). Je peux te montrer comment faire si ça t'intéresse.
- **Alertes** : le bot pourrait aussi poster dans le salon général quand un item passe sous un certain seuil.
