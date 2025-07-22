import { marked } from "marked";

// Convertit le markdown en HTML interprétable
export function formatSummaryText(markdownText) {
  const html = marked.parse(markdownText);
  return html;
}
