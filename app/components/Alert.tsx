'use client';
import React, { useState } from "react";
import Image from "next/image";
import styles from './Alert.module.css';
const Alert = () => {
  const[showAlert, setAlertDismiss] = useState(true);
  const handleAlertDismiss = () =>setAlertDismiss(false);
  return (
    showAlert && (<div className={`bg-udemyPurple text-white p-4 flex px-9 w-screen max-sm:text-sm text-base`}>
      <div className="flex justify-center flex-grow"><a href="#"><span className={`${styles.fontsBold}`}>Ready to get with the times?</span> | Get the skills with Udemy Business.</a></div>
      <div className="flex justify-end"><button onClick = {handleAlertDismiss} >
        <Image
            src={"/close.svg"}
            alt="Close"
            className="invert"
            width={25}
            height={25}
            priority
        />
        </button></div>
    </div>)
  );
};

export default Alert;
