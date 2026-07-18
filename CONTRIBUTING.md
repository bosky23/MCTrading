# Comment ajouter un prix

1. Va sur `data/prices.json` dans le repo GitHub.
2. Clique sur l'icône crayon (✏️) en haut à droite pour éditer.
3. Ajoute une nouvelle ligne à la fin de la liste, au même format que les autres :

```json
{ "item": "Diamant", "prix": 130, "date": "2026-07-16T09:00:00Z" }
```

- `item` : le nom exact affiché dans le shop en jeu.
- `prix` : un nombre (sans texte, sans virgule).
- `date` : la date et l'heure du relevé, au format `AAAA-MM-JJTHH:MM:SSZ`.

4. En bas de page, GitHub te proposera de créer une **branche** et d'ouvrir une **pull request** (PR). Choisis cette option.
5. Une fois la PR ouverte, un contrôle automatique vérifie que ton format est correct.
6. Si tout est bon, la PR est fusionnée (mergée) et le site se met à jour automatiquement.

Pas besoin d'installer Git ni de connaître le code : tout se fait depuis le navigateur.
