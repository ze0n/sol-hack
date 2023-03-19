import {
    ConnectionProvider,
    WalletProvider,
    useConnection,
    useWallet,
  } from '@solana/wallet-adapter-react';
  import { PhantomWalletAdapter } from '@solana/wallet-adapter-phantom';
  import { clusterApiUrl } from '@solana/web3.js';
  
  export const SolanaConnectionProvider = ConnectionProvider;
  export const SolanaWalletProvider = WalletProvider;
  export const useSolanaConnection = useConnection;
  export const useSolanaWallet = useWallet;
  
  export const SOLANA_NETWORK = 'devnet';
  export const SOLANA_RPC_URL = clusterApiUrl(SOLANA_NETWORK);
  export const SOLANA_WALLET_ADAPTERS = [PhantomWalletAdapter];
  