
import Head from "next/head";
import FileUpload from "../components/FileUpload";
import ChatInterface from "../components/ChatInterface";

export default function Home() {
  return (
    <div>
      <Head>
        <title>Financial Q&A</title>
      </Head>
      <main>
        <h1>Financial Statement Q&A</h1>
        <FileUpload />
        <ChatInterface />
      </main>
    </div>
  );
}
