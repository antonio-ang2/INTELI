// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

const lightCodeTheme = require("prism-react-renderer/themes/github");
const darkCodeTheme = require("prism-react-renderer/themes/dracula");

const organizationName = "2023M8T2-Inteli"; // Usually your GitHub org/user name.
const projectName = "grupo6"; // Usually your repo name.

/** @type {import('@docusaurus/types').Config} */
const config = {
  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.

  title: "Chauffeur",
  tagline: "Robótica móvel e deep learning",
  favicon: "img/inteli.svg",
  url: `https://${organizationName}.github.io`,
  baseUrl: `/${projectName}/`,

  organizationName: "2023M8T2-Inteli", // Usually your GitHub org/user name.
  projectName: "grupo6", // Usually your repo name.

  onBrokenLinks: "throw",
  onBrokenMarkdownLinks: "warn",

  // Even if you don't use internalization, you can use this field to set useful
  // metadata like html lang. For example, if your site is Chinese, you may want
  // to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: "en",
    locales: ["en"],
  },

  presets: [
    [
      "classic",
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          routeBasePath: "/",
          sidebarPath: require.resolve("./sidebars.js"),
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            "https://github.com/${organizationName}/${projectName}/tree/main/docs",
        },
        blog: false,
        theme: {
          customCss: require.resolve("./src/css/custom.css"),
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      // Replace with your project's social card
      image: "img/docusaurus-social-card.jpg",
      navbar: {
        title: "Chauffeur",
        logo: {
          alt: "Logo Inteli",
          src: "img/inteli.svg",
        },
        items: [
          {
            type: "docSidebar",
            sidebarId: "tutorialSidebar",
            position: "left",
            label: "Material de Computação",
          },
          {
            href: "https://github.com/2023M8T2-Inteli/grupo6",
            label: "GitHub",
            position: "right",
          },
        ],
      },
      footer: {
        style: "dark",
        copyright: `Copyright © ${new Date().getFullYear()} Módulo 8. Built with Docusaurus.`,
      },
      prism: {
        theme: lightCodeTheme,
        darkTheme: darkCodeTheme,
        magicComments: [
          // Remember to extend the default highlight class name as well!
          {
            className: "theme-code-block-highlighted-line",
            line: "highlight-next-line",
            block: { start: "highlight-start", end: "highlight-end" },
          },
          {
            className: "code-block-red",
            line: "red",
          },
          {
            className: "code-block-green",
            line: "green",
          },
          {
            className: "code-block-blue",
            line: "blue",
          },
          {
            className: "code-block-purple",
            line: "purple",
          },
        ],
      },
    }),
};

module.exports = config;
