import { Roboto } from "next/font/google";

const roboto_init = Roboto({ 
    subsets: ["latin"],
    weight: ["100","300","400","500","700","900"]
});

export const roboto = roboto_init.className;