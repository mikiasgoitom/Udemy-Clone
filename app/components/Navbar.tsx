import Image from "next/image";
import React from "react";

const Navbar = () => {
  return (
    <div className="navbar bg-base-100 flex flex-row justify-between px-8 w-auto drop-shadow-lg

    ">
      <div className="flex justify-start">
        <a>
          <Image
            src="/logo-udemy.svg"
            alt="Udemy Logo"
            width={100}
            height={24}
            priority
          />
        </a>
        <div className="dropdown dropdown-hover">
          <div
            tabIndex={0}
            role="button"
            className="mx-7 hover:text-udemyPurple"
          >
            <span>Catagories</span>
          </div>
          <ul
            tabIndex={0}
            className="dropdown-content z-[1] menu p-2 shadow bg-base-100 w-52"
          >
            <li>
              <a>Item 1</a>
            </li>
            <li>
              <a>Item 2</a>
            </li>
          </ul>
        </div>
      </div>
      {/* search functionality */}
      <div className="border-solid border-black border rounded-3xl w-auto flex-1">
        <div className="form-control p-3 flex flex-grow flex-row justify-between">
          <div>
            <Image
              src="/search.svg"
              alt="Search"
              className="invert"
              height={23}
              width={23}
              priority
            />
          </div>
          <div className="flex-grow ml-2">
            <input
              type="text"
              className="text-sm placeholder-gray-500 bg-transparent w-full"
              placeholder="Search for anything"
            />
          </div>
        </div>
      </div>
      <div className="flex justify-end">
        {/* text  */}
        <div className="dropdown dropdown-hover">
          <div
            tabIndex={0}
            role="button"
            className="ml-5 hover:text-udemyPurple"
          >
            <span>Udemy Business</span>
          </div>
          <div
            tabIndex={0}
            className="dropdown-content z-[1] menu p-2 shadow bg-base-100 w-64 font-bold"
          >
            <p className="text-lg text-center tracking-wide mt-1">
              Get your team access to over 25,000 top Udemy courses, anytime,
              anywhere.
            </p>
            <button className="btn btn-wide rounded-none btn-neutral mt-3 text-lg text-white">
              Try Udemy Business
            </button>
          </div>
        </div>
        {/* text  */}
        <div className="dropdown dropdown-hover">
          <div
            tabIndex={0}
            role="button"
            className="mx-7 hover:text-udemyPurple"
          >
            <span>Teach on Udemy</span>
          </div>
          <div
            tabIndex={0}
            className="dropdown-content z-[1] menu p-2 shadow bg-base-100 w-64 font-bold"
          >
            <p className="text-lg text-center tracking-wide mt-1">
              Turn what you know into an opportunity and reach millions around
              the world.
            </p>
            <button className="btn btn-wide rounded-none btn-neutral mt-3 text-lg text-white">
              Learn more
            </button>
          </div>
        </div>
        {/* cart icon */}
        <div className="dropdown dropdown-hover mr-6">
          <div tabIndex={0} role="button" className="pt-2">
            <div className="indicator">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className="h-6 w-6 hover:stroke-udemyPurple"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth="2"
                  d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"
                />
              </svg>
              {/* <span className="badge badge-sm indicator-item">8</span> */}
            </div>
          </div>
          <div
            tabIndex={0}
            className="mt-3 z-[1] card card-compact dropdown-content w-52 bg-base-100 shadow"
          >
            <div className="card-body">
              <span className="text-sm text-center tracking-wide font-semibold text-gray-500">
                Your cart is empty
              </span>
              <div className="card-actions">
                <a
                  className="text-center text-udemyPurple font-semibold tracking-wide "
                  href="#"
                >
                  Keep shopping
                </a>
              </div>
            </div>
          </div>
        </div>
        {/* buttons  */}
        <div className="btn btn-ghost font-bold rounded-none border border-solid border-black hover:border-black mx-1">
          Log in
        </div>
        <div className="btn btn-neutral font-bold text-white rounded-none mx-1">
          Sign up
        </div>
        <div className="btn btn-ghost rounded-none border border-solid border-black hover:border-black mx-1">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width={24}
            height={24}
            fill="black"
            viewBox="0 -960 960 960"
          >
            <path d="M480-80q-82 0-155-31.5t-127.5-86Q143-252 111.5-325T80-480q0-83 31.5-155.5t86-127Q252-817 325-848.5T480-880q83 0 155.5 31.5t127 86q54.5 54.5 86 127T880-480q0 82-31.5 155t-86 127.5q-54.5 54.5-127 86T480-80Zm0-82q26-36 45-75t31-83H404q12 44 31 83t45 75Zm-104-16q-18-33-31.5-68.5T322-320H204q29 50 72.5 87t99.5 55Zm208 0q56-18 99.5-55t72.5-87H638q-9 38-22.5 73.5T584-178ZM170-400h136q-3-20-4.5-39.5T300-480q0-21 1.5-40.5T306-560H170q-5 20-7.5 39.5T160-480q0 21 2.5 40.5T170-400Zm216 0h188q3-20 4.5-39.5T580-480q0-21-1.5-40.5T574-560H386q-3 20-4.5 39.5T380-480q0 21 1.5 40.5T386-400Zm268 0h136q5-20 7.5-39.5T800-480q0-21-2.5-40.5T790-560H654q3 20 4.5 39.5T660-480q0 21-1.5 40.5T654-400Zm-16-240h118q-29-50-72.5-87T584-782q18 33 31.5 68.5T638-640Zm-234 0h152q-12-44-31-83t-45-75q-26 36-45 75t-31 83Zm-200 0h118q9-38 22.5-73.5T376-782q-56 18-99.5 55T204-640Z" />
          </svg>
        </div>
      </div>
    </div>
  );
};

export default Navbar;
