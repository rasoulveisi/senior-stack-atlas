# Senior Stack Atlas

A visual guide to senior engineering interviews, built from three real production codebases:

- **PhysioCoach AI**: Express 5, TypeScript, Cloudflare Workers, Hyperdrive, Drizzle, Neon PostgreSQL
- **Job Craft**: .NET 10 Minimal APIs, EF Core, pgvector, `Channel<T>`, Angular 20
- **Next Issue Tracker**: React 19, Next.js 16.4, React Compiler, Drizzle, PGlite

The page has 29 chapters, a cross-stack comparison map and 58 interview answers. Every answer is visible on the page.
It teaches with diagrams, charts, animated flows, real code and short B1–B2 English.

## Folder layout

```text
index.html            the page (GitHub Pages serves this file)
assets/site.css       compiled Tailwind CSS
favicon.svg           browser tab icon
.nojekyll             tells GitHub Pages to serve the files as they are
src/parts/            the source of the page, one file per part
src/styles.css        Tailwind input: palette components and custom CSS
src/build.py          joins src/parts into index.html
tailwind.config.js    colours (storm, vivid, coral) and fonts
package.json          build scripts
.agent-work/          build cards and audit reports from the first build (ignored by git)
```

## Publish on GitHub Pages

1. Create an empty repository on GitHub, for example `senior-stack-atlas`.
2. Push the contents of this folder to the `main` branch of that repository.
3. On GitHub, open **Settings → Pages**.
4. Under **Build and deployment**, set **Source** to **Deploy from a branch**.
5. Set the branch to `main` and the folder to `/ (root)`, then select **Save**.
6. Wait one or two minutes. The site opens at `https://<your-user>.github.io/senior-stack-atlas/`.

GitHub Pages does not run any build. It serves the committed `index.html` and `assets/site.css`, so commit both after each change.

## Edit and rebuild

1. Change a file in `src/parts/` (for example `21-dotnet-a.html` for .NET chapters 2.1–2.5).
2. Install the Tailwind compiler once: `npm install`.
3. Rebuild the page and the CSS: `npm run build`.
4. Preview locally: `npm run serve`, then open `http://localhost:8000`.

Run `npm run build` after every change. The CSS contains only the Tailwind classes that `index.html` uses, so a new class has no style until you rebuild.

`src/parts/_kit.html` is the design kit: every component (callouts, flows, charts, code blocks, interview cards, SVG rules) with its markup. It is a reference for new chapters and is not part of the page.

## External resources

The page loads these at runtime, so it needs an internet connection:

- Google Fonts: Lexend and JetBrains Mono
- highlight.js 11.9.0 from cdnjs (code colours)
- Lucide 0.460.0 from unpkg (icons)
