use anchor_lang::prelude::*;

declare_id!("4EqNfDwKUmatpyaNU3Z2ueYPiSMuWLZyvdJbwYcdKDpX");

#[program]
mod restaurant_goal {
    use super::*;
    pub fn set_goal(ctx: Context<GoalAccounts>, restaurant: String, amount: u64) -> Result<()> {
        let new_goal = &mut ctx.accounts.goal;
        new_goal.winner = ctx.accounts.signer.key();
        new_goal.loser = ctx.accounts.loseFund.key();
        new_goal.escrow = ctx.accounts.tempFund.key();
        new_goal.amount = amount;
        new_goal.status = 0;

        msg!("Restaurant goal for {} stars", new_goal.amount);

        msg!(
            "Signer {}: {}",
            ctx.accounts.signer.key(),
            ctx.accounts.signer.lamports()
        );
        msg!(
            "Temp {}: {}",
            ctx.accounts.tempFund.key(),
            ctx.accounts.tempFund.lamports()
        );

        msg!(
            "Sending {} --> {}",
            ctx.accounts.signer.key(),
            ctx.accounts.tempFund.key()
        );

        let ix = anchor_lang::solana_program::system_instruction::transfer(
            &ctx.accounts.signer.key(),
            &ctx.accounts.tempFund.key(),
            amount,
        );

        anchor_lang::solana_program::program::invoke(
            &ix,
            &[
                ctx.accounts.signer.to_account_info(),
                ctx.accounts.tempFund.to_account_info(),
            ],
        );

        Ok(())
    }

    pub fn finish_goal(ctx: Context<GoalAccounts>, status: u8) -> Result<()> {
        if status == 1 {
            ctx.accounts.goal.status = status;
            msg!(
                "Won, transfering amount {} --> {}",
                ctx.accounts.goal.amount,
                ctx.accounts.goal.winner
            );

            let ix = anchor_lang::solana_program::system_instruction::transfer(
                &ctx.accounts.tempFund.key(),
                &ctx.accounts.signer.key(), // winner
                ctx.accounts.goal.amount,
            );

            anchor_lang::solana_program::program::invoke(
                &ix,
                &[
                    ctx.accounts.tempFund.to_account_info(),
                    ctx.accounts.signer.to_account_info(), // winner
                ],
            );
        } else if status == 2 {
            msg!(
                "Failed, transfering amount {} --> {}",
                ctx.accounts.goal.amount,
                ctx.accounts.goal.loser
            );
            let ix = anchor_lang::solana_program::system_instruction::transfer(
                &ctx.accounts.tempFund.key(),
                &ctx.accounts.loseFund.key(),
                ctx.accounts.goal.amount,
            );

            anchor_lang::solana_program::program::invoke(
                &ix,
                &[
                    ctx.accounts.tempFund.to_account_info(),
                    ctx.accounts.loseFund.to_account_info(),
                ],
            );
        }
        Ok(())
    }
}

#[derive(Accounts)]
#[instruction(restaurant: String)]
pub struct GoalAccounts<'info> {
    #[account(
        init_if_needed,
        payer = signer,
        space = 500,
        seeds = [restaurant.as_bytes().as_ref(), signer.key().as_ref()],
        bump
    )]
    pub goal: Account<'info, Goal>,

    #[account(mut)]
    pub tempFund: UncheckedAccount<'info>,

    #[account(mut)]
    pub loseFund: UncheckedAccount<'info>,

    #[account(mut)]
    pub signer: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[account]
pub struct Goal {
    pub winner: Pubkey,
    pub loser: Pubkey,
    pub escrow: Pubkey,
    pub amount: u64,
    pub status: u8,
}

// #[account]
// pub struct Goal {
//     pub winnerAddress: Pubkey,
//     pub fundAddress: Pubkey,
//     pub amount: u64,
//     pub status: u8,
//     //pub externalGoalId: u128
// }

// #[program]
// mod restaurant_goal {
//     use super::*;
//     pub fn set_goal(ctx: Context<GoalAccounts>, amount: u64) -> Result<()> {
//         let new_goal = &mut ctx.accounts.goal;

//         new_goal.winnerAddress = ctx.accounts.signer.key();
//         new_goal.fundAddress = ctx.accounts.signer.key();
//         new_goal.amount = amount;
//         new_goal.status = 0;

//         //msg!("New goal set for {} - {} stars", new_goal.winner_address, new_goal.amount);
//         //msg!("Goal: {}", new_goal);

//         Ok(())
//     }
// }

// #[derive(Accounts)]
// #[instruction()]
// pub struct GoalAccounts<'info> {
//     #[account(
//         init_if_needed,
//         payer = signer,
//         space = 500,
//         seeds = ['Goal', signer.key().as_ref()],
//         bump
//     )]
//     pub goal: Account<'info, Goal>,
//     #[account(mut)]
//     pub signer: Signer<'info>,
//     pub system_program: Program<'info, System>,
// }

// #[account]
// pub struct Goal {
//   pub winnerAddress: Pubkey,
//   pub fundAddress: Pubkey,
//   pub amount: u64,
//   pub status: u8,
//   //pub externalGoalId: u128
// }
