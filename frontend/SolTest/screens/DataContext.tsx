import React, { createContext, useState, Dispatch, SetStateAction } from 'react';

interface IDataContext {
  selectedSteps: number;
  setSelectedSteps: Dispatch<SetStateAction<number>>;
  amount: string;
  setAmount: Dispatch<SetStateAction<string>>;
}

export const DataContext = createContext<IDataContext | null>(null);

export const DataProvider: React.FC = ({ children } : any) => {
  const [selectedSteps, setSelectedSteps] = useState<number>(0);
  const [amount, setAmount] = useState<string>('');

  return (
    <DataContext.Provider value={{ selectedSteps, setSelectedSteps, amount, setAmount }}>
      {children}
    </DataContext.Provider>
  );
};
