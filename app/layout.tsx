import type { Metadata } from "next";
import { roboto } from './utils/fonts';
import "./globals.css";


export const metadata: Metadata = {
  title: "Udemy",
  description: "IP_2 Assignment",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
